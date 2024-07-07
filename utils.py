DB_password='Muaaz123'
database_name='company_info'
api_key='d5df8117-8f78-44a9-ba97-848a2611a2b3'
chunk_size=500
chunk_overlap=50
embed_model='BAAI/bge-small-en-v1.5'

from pydantic import BaseModel

class company_info(BaseModel):
    company_name:str
    CR_number:int
    email:str

class PDFUrl(BaseModel):
    url: str
    company_name: str