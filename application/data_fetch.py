from langchain_community.document_loaders.csv_loader import CSVLoader
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
import json
import os
root_dir = 'data'

chunk_counter = 0

# Documents = {"pdf": [], "text": [], "csv": []}
char_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=40)


def dump_chunks(chunks, output_path, prefix):
    global chunk_counter
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    output = []
    for chunk_index, chunk in enumerate(chunks):
        chunk_counter += 1
        chunk_id = f"{prefix}_{chunk_counter}"
        chunk.id = chunk_id
        output.append(chunk.model_dump())

    with open(output_path, "w") as f:
        json.dump(output, f, indent=4)


def load_and_split_pdf(file_path):
    loader = PyPDFLoader(file_path)
    file_key = os.path.splitext(os.path.basename(file_path))[0]

    for page_id, data in enumerate(loader.lazy_load()):
        chunks = char_splitter.split_documents([data])
        output_file = f"Chunks/pdf/{file_key}_page_{page_id}.json"
        dump_chunks(chunks, output_file, f"pdf_{file_key}_page_{page_id}")


def load_and_split_text(file_path):
    loader = TextLoader(file_path, encoding="utf-8")
    file_key = os.path.splitext(os.path.basename(file_path))[0]
    chunks = []

    for doc in loader.lazy_load():
        chunks.extend(char_splitter.split_documents([doc]))

    output_file = f"Chunks/text/{file_key}.json"
    dump_chunks(chunks, output_file, f"text_{file_key}")


def process_files(root_dir):
    for dir in os.scandir(root_dir):
        if dir.is_dir():
            folder_name = dir.name
        else:
            continue

        for file in os.scandir(dir):
            if folder_name == "pdf":
                print(f"Processing {file.name} with pdf loader")
                load_and_split_pdf(file.path)
            elif folder_name == "text":
                print(f"Call Text loader for file {file.name}")
                load_and_split_text(file.path)
            # elif folder_name == "csv":
            #     print(f"Call CSV loader for file {file.name}")
            #     # Implement CSV loading and splitting logic here



