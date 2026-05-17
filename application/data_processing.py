from langchain_community.document_loaders import PyPDFDirectoryLoader 
import os 
from application.vector_store import get_vector_store
from application.splitter import get_pdf_splitter




def process_folders(dir_name = "data"):
    path = os.path.abspath(dir_name)

    if not os.path.exists(path):
        raise FileNotFoundError
    
    for dir in os.scandir(path):
        if not dir.is_dir():
            continue 
        if dir.name == "pdf":
            print(f"Processing pdf directory")
            process_pdf_dir(os.path.join(path,dir.name))
            


def process_pdf_dir(path):
    BATCH_SIZE = 50 
    chunk_accumulator = []
    splitter = get_pdf_splitter()
    loader = PyPDFDirectoryLoader(path)
    vector_store = get_vector_store()
    
    for page in loader.lazy_load():
        page_chunks = splitter.split_documents([page])

        if len(chunk_accumulator) >= BATCH_SIZE:
            vector_store.add_documents(chunk_accumulator)
            chunk_accumulator = []
        
        chunk_accumulator.extend(page_chunks)

    vector_store.add_documents(chunk_accumulator)


