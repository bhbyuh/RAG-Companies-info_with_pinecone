from utils import api_key
from pinecone import Pinecone, ServerlessSpec

def Pinecone_index_creation(Index_name,dimensions):
    print("IN pineconn")
    pc = Pinecone(api_key=api_key)

    index_name = Index_name
    dimension = dimensions

    if index_name not in pc.list_indexes().names():
        pc.create_index(
            name=index_name,
            dimension=dimension,
            metric='cosine',
            spec=ServerlessSpec(
                cloud='aws',
                region='us-east-1'
            )
        )
        print("Index created successfully.")
    else:
        print("Index already exists.")

def get_Pine_cone_object(apikey):
    pin=Pinecone(api_key=apikey)
    return pin

def pine_cone_index_checker(apikey,CR_number):
    pc=Pinecone(api_key=apikey)
    
    if CR_number in pc.list_indexes().names():
        return True
    return False

def put_data(indexname,split_text,embedding_model,pineconee):
    index=pineconee.Index('as')
    
    embeddings=list()
    for split in split_text:
        embeddings.append(embedding_model.embed_query(split))
    print("embeddinggs done")
    vectors=list()
    for i,(split,embedding) in enumerate(zip(split_text,embeddings)):
        vector = {
        "id": str(i),
        "values": embedding,
        "metadata": {"text": split}
        }
        
        vectors.append(vector)
    
    index.upsert(vectors)
