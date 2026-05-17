from langchain_huggingface import HuggingFaceEmbeddings
from dotenv import load_dotenv
load_dotenv()

def get_embedding():
    return HuggingFaceEmbeddings(model_name="sentence-transformers/all-mpnet-base-v2")