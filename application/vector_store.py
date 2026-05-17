from langchain_pinecone import PineconeVectorStore 
from pinecone import Pinecone , ServerlessSpec
from embeddings import get_embedding    
import os 

def get_vector_store(index_name = 'ragagent'):
    pc = Pinecone(api_key=os.environ.get("PINECONE_KEY")) 
    
    # create index if not exists
    if index_name not in [index['name'] for index in  pc.list_indexes()]:
        pc.create_index(
            name=index_name,
            vector_type="dense",
            dimension=768,
            metric="cosine",
            spec=ServerlessSpec(
                cloud="aws",
                region="us-east-1"
            ),
            deletion_protection="disabled",
            tags={
                "environment": "development"
            }
        )

    
    return PineconeVectorStore(embedding=get_embedding() , index= pc.Index(index_name), namespace='default')


