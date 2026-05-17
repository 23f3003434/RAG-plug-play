from langchain_text_splitters import RecursiveCharacterTextSplitter



def get_pdf_splitter(s = 500 , o = 40):
    return RecursiveCharacterTextSplitter(chunk_size=s, chunk_overlap=o)
