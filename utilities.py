from langchain_community.document_loaders import PyMuPDFLoader
from langchain.text_splitter import  CharacterTextSplitter
from langchain.docstore.document import Document
from pinecone import Pinecone

def file_loader(file_path):
    loader=PyMuPDFLoader(file_path)
    pages=loader.load()
    return pages

def doc_splitter(pages,chunk_size,chunk_overlap):
    
    splitter=CharacterTextSplitter(
    separator='\n',
    chunk_size=chunk_size,
    chunk_overlap=chunk_overlap,
    length_function=len
    )

    doc_list = []
    for page in pages:
        page_splits = splitter.split_text(page.page_content)
        doc_list.extend(page_splits)
    
    return doc_list

def url_splitter(pages,chunk_size,chunk_overlap):
    splitter=CharacterTextSplitter(
    separator='\n',
    chunk_size=chunk_size,
    chunk_overlap=chunk_overlap,
    length_function=len
    )

    doc_list = []
    for page in pages:
        page_splits = splitter.split_text(page)
        doc_list.extend(page_splits)
    
    return doc_list