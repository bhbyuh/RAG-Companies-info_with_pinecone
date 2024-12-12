# Document Interaction Platform - Backend Development  

## Introduction  
This repository contains the backend implementation for a **Document Interaction Platform**, enabling companies to upload their documents to the platform and allowing their employees to interact with these documents through a conversational AI interface.  

## Description  
The platform's backend is built using modern technologies to support document uploads, storage, and interaction. The system leverages **FastAPI** for developing APIs, **LangChain** and the **Ollama Phi3** model for language modeling, and **Pinecone** as a vector database for efficient document search and retrieval. Additionally, **PostgreSQL** is used for storing structured data in a relational database.  

### Key Features:  
1. **Document Upload:**  
   - Companies can upload documents (e.g., PDFs, Word files).  
   - The uploaded documents are processed and stored in the vector database for efficient search.  

2. **Interactive Conversations:**  
   - Employees can query the system and interact with uploaded documents conversationally.  
   - The system retrieves relevant information from the documents using **LangChain** and reranks results with the **Ollama Phi3** model.  

3. **Search and Retrieval:**  
   - **Semantic Search:** Combines vector similarity from **Pinecone**.

## Tools and Technologies  
- **Backend Framework:** FastAPI  
- **Language Modeling:** LangChain, Ollama Phi3  
- **Vector Database:** Pinecone  
- **Relational Database:** PostgreSQL  
- **Programming Language:** Python  
- **Libraries and Tools:**  
  - PyPDF2 (or equivalent) for document parsing  

## How It Works  
1. **Document Upload:**  
   - Company uploads documents to the platform.  
   - Documents are parsed and vectorized before being stored in **Pinecone**. Metadata is stored in **PostgreSQL**.  

2. **Query Handling:**  
   - Employees query the platform through a conversational interface.  
   - The query is processed using **LangChain**, and relevant document embeddings are retrieved from **Pinecone**.  
   - Results are reranked using the **Ollama Phi3** model for improved accuracy.  

3. **Response Generation:**  
   - The system returns the most relevant sections of the documents to the user.  

4. **API Endpoints:**  
   - **Upload Endpoint:** For document uploads and processing.  
   - **Query Endpoint:** For employees to interact with documents.  
