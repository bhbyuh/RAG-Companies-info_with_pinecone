from fastapi import FastAPI,UploadFile,File,Form,HTTPException
from fastapi.responses import JSONResponse
from utils import *
import uvicorn
from Queries import table_creation,company_data_insertion
from DB_Connection import session_making
from pinecon import Pinecone_index_creation,get_Pine_cone_object,pine_cone_index_checker,put_data
import tempfile
from utilities import file_loader,doc_splitter,url_splitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from pydantic import BaseModel
import requests
import fitz  # PyMuPDF
import io

app=FastAPI()

embedding_model=HuggingFaceEmbeddings(model_name=embed_model)

@app.get('/')
def start():
    return ("Welecome to Landing Page")

#def company_creation(data:company_info):
#data=[company_info.CR_number,company_info.company_name,company_info.email]
@app.get('/getcompanydata')
def  company_creation(CR_number:int ,company_name:str,email:str):
    
    data=[CR_number,company_name,email]
    conn,cur=session_making(DB_password,database_name)
    
    if(company_data_insertion(data,conn,cur)):
        Pinecone_index_creation(company_name,384)
        output="Successfully Registered"
    else:
        output="Company is Already Registered"

    return JSONResponse(content={"Message":output})

@app.post('/upload_file')
async def get_pdf(company_name:str=Form(...), file: UploadFile=File(...)):
    if (pine_cone_index_checker(api_key,company_name)):
        contents=await file.read()

        with tempfile.NamedTemporaryFile(delete=False,suffix=".pdf") as tmp_file:
            tmp_file.write(contents)
        
        pages=file_loader(tmp_file.name)
        split_text=doc_splitter(pages,chunk_size,chunk_overlap)
        
        pinecone_object=get_Pine_cone_object(api_key)

        put_data(company_name,split_text,embedding_model,pinecone_object)

        return JSONResponse({"Message":"File Successful upload"})
    else:
        return JSONResponse({"Message":"Company with that CR already available"})

@app.post("/Pdf_url")
async def extract_text_from_pdf(company_name:str,pdf_url:str):
    if (pine_cone_index_checker(api_key,company_name)):
        # PDF Download
        response = requests.get(pdf_url)
        response.raise_for_status()

        pdf_document = fitz.open(stream=response.content, filetype="pdf")

        text = list()
        for page_num in range(len(pdf_document)):
            page = pdf_document.load_page(page_num)
            text.append(page.get_text())
        
        split_text=url_splitter(text,chunk_size,chunk_overlap)

        pinecone_object=get_Pine_cone_object(api_key)

        put_data(company_name,split_text,embedding_model,pinecone_object)

        return JSONResponse({'Message':"Data Successful upload"})
    else:
        return JSONResponse({'Message':"Company with that CR already available"})


if __name__ == "__main__":
    conn,cur=session_making(DB_password,database_name)
    table_creation(conn,cur)
    
    uvicorn.run(app, host="127.0.0.1", port=8000)