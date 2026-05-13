# Simple Plug & Play RAG

A lightweight **Retrieval-Augmented Generation (RAG)** pipeline built using LangChain with automated document ingestion, chunking, embedding generation, and vector storage using Pinecone.

This project focuses primarily on the **data ingestion and retrieval pipeline** rather than frontend UI or conversational memory management.

---

## Features

* Automatic document ingestion from local directories
* Recursive document chunking pipeline
* Embedding generation using open-source Hugging Face embedding models
* Dense vector storage in Pinecone
* Hybrid Retrieval Architecture (Dense + BM25) *(BM25 integration in progress)*
* Organized chunk storage by file type and filename
* Modular and extensible LangChain-based architecture

---

# Architecture Overview

```text
Local Documents
       │
       ▼
Document Loader
       │
       ▼
Text Chunking
       │
       ▼
HuggingFace Embeddings
       │
       ▼
Pinecone Vector Index
       │
       ▼
Retriever (Dense + BM25 Hybrid)
       │
       ▼
LLM / Agent
```

---

# Supported File Types

Currently supported:

* PDF
* CSV
* TXT / Text files

---

# Project Structure

```bash
project-root/
│
├── data/
│   ├── pdf/
│   ├── csv/
│   └── text/
│
├── chunks/
│
├── data_fetch.py
├── ingest.py
├── retriever.py
├── requirements.txt
└── README.md
```

---

# How It Works

## 1. Data Loading

* The pipeline automatically scans the `data/` directory
* Documents are loaded into LangChain `Document` objects
* Separate loaders are used based on file type
* For debugging/testing purposes, merged processed data can optionally be exported as JSON

### Data Directory Format

```bash
data/
├── pdf/
├── csv/
└── text/
```

Place your files inside their corresponding folders.

---

## 2. Document Chunking

Documents are automatically split into smaller chunks for efficient retrieval.

Features:

* Recursive chunk splitting
* Configurable chunk size and overlap
* Chunk organization by:

  * file type
  * source filename

You can tune chunking parameters inside:

```python
data_fetch.py
```

Example parameters:

```python
chunk_size = 1000
chunk_overlap = 200
```

---

## 3. Embeddings

The project uses open-source embedding models from Hugging Face.

Current setup supports:

* Sentence Transformers
* HuggingFace Embeddings via LangChain

Example:

```python
from langchain.embeddings import HuggingFaceEmbeddings
```

---

## 4. Vector Storage

Dense embeddings are uploaded to a Pinecone index for semantic retrieval.

Current status:

| Retrieval Type        | Status              |
| --------------------- | ------------------- |
| Dense Vector Search   | ✅ Implemented       |
| BM25 Sparse Retrieval | 🚧 Work in Progress |
| Hybrid Retrieval      | 🚧 Partial          |

---

# Installation

## Clone Repository

```bash
git clone <your-repo-url>
cd <project-folder>
```

---

## Create Virtual Environment

```bash
python -m venv venv
```

### Activate Environment

#### Windows

```bash
venv\Scripts\activate
```

#### Linux / macOS

```bash
source venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Environment Variables

Create a `.env` file in the project root:

```env
PINECONE_API_KEY=your_api_key
PINECONE_ENVIRONMENT=your_environment
OPENAI_API_KEY=your_key_if_using_llm
```

---

# Running the Pipeline

## Step 1 — Add Documents

Place files inside:

```bash
data/pdf
data/csv
data/text
```

---

## Step 2 — Run Ingestion

```bash
python ingest.py
```

This will:

* Load documents
* Create chunks
* Generate embeddings
* Upload vectors to Pinecone

---

## Step 3 — Run Retrieval

```bash
python retriever.py
```

---

# Current Limitations

* Local file loaders only
* Sparse vector indexing not fully implemented
* No frontend/chat UI
* No persistent conversation memory
* No reranking pipeline yet

---

# Future Improvements

* Full Hybrid Retrieval (Dense + BM25)
* Sparse vector storage support
* Metadata filtering
* Reranking models
* Streaming responses
* Conversational memory
* Web UI integration
* Multi-modal document support

---

# Tech Stack

* Python
* LangChain
* Pinecone
* Hugging Face
* Sentence Transformers

---

# Use Case

This project is useful for:

* Internal knowledge base systems
* Enterprise document search
* AI assistants
* Semantic search pipelines
* Research document retrieval

---

# Status

🚧 Active Development — Retrieval pipeline functional, hybrid search under development.
# Simple Plug & Play RAG

A lightweight **Retrieval-Augmented Generation (RAG)** pipeline built using LangChain with automated document ingestion, chunking, embedding generation, and vector storage using Pinecone.

This project focuses primarily on the **data ingestion and retrieval pipeline** rather than frontend UI or conversational memory management.

---

## Features

* Automatic document ingestion from local directories
* Recursive document chunking pipeline
* Embedding generation using open-source Hugging Face embedding models
* Dense vector storage in Pinecone
* Hybrid Retrieval Architecture (Dense + BM25) *(BM25 integration in progress)*
* Organized chunk storage by file type and filename
* Modular and extensible LangChain-based architecture

---

# Architecture Overview

```text
Local Documents
       │
       ▼
Document Loader
       │
       ▼
Text Chunking
       │
       ▼
HuggingFace Embeddings
       │
       ▼
Pinecone Vector Index
       │
       ▼
Retriever (Dense + BM25 Hybrid)
       │
       ▼
LLM / Agent
```

---

# Supported File Types

Currently supported:

* PDF
* CSV
* TXT / Text files

---

# Project Structure

```bash
project-root/
│
├── data/
│   ├── pdf/
│   ├── csv/
│   └── text/
│
├── chunks/
│
├── data_fetch.py
├── ingest.py
├── retriever.py
├── requirements.txt
└── README.md
```

---

# How It Works

## 1. Data Loading

* The pipeline automatically scans the `data/` directory
* Documents are loaded into LangChain `Document` objects
* Separate loaders are used based on file type
* For debugging/testing purposes, merged processed data can optionally be exported as JSON

### Data Directory Format

```bash
data/
├── pdf/
├── csv/
└── text/
```

Place your files inside their corresponding folders.

---

## 2. Document Chunking

Documents are automatically split into smaller chunks for efficient retrieval.

Features:

* Recursive chunk splitting
* Configurable chunk size and overlap
* Chunk organization by:

  * file type
  * source filename

You can tune chunking parameters inside:

```python
data_fetch.py
```

Example parameters:

```python
chunk_size = 1000
chunk_overlap = 200
```

---

## 3. Embeddings

The project uses open-source embedding models from Hugging Face.

Current setup supports:

* Sentence Transformers
* HuggingFace Embeddings via LangChain

Example:

```python
from langchain.embeddings import HuggingFaceEmbeddings
```

---

## 4. Vector Storage

Dense embeddings are uploaded to a Pinecone index for semantic retrieval.

Current status:

| Retrieval Type        | Status              |
| --------------------- | ------------------- |
| Dense Vector Search   | ✅ Implemented       |
| BM25 Sparse Retrieval | 🚧 Work in Progress |
| Hybrid Retrieval      | 🚧 Partial          |

---

# Installation

## Clone Repository

```bash
git clone <your-repo-url>
cd <project-folder>
```

---

## Create Virtual Environment

```bash
python -m venv venv
```

### Activate Environment

#### Windows

```bash
venv\Scripts\activate
```

#### Linux / macOS

```bash
source venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Environment Variables

Create a `.env` file in the project root:

```env
PINECONE_API_KEY=your_api_key
PINECONE_ENVIRONMENT=your_environment
OPENAI_API_KEY=your_key_if_using_llm
```

---

# Running the Pipeline

## Step 1 — Add Documents

Place files inside:

```bash
data/pdf
data/csv
data/text
```

---

## Step 2 — Run Ingestion

```bash
python ingest.py
```

This will:

* Load documents
* Create chunks
* Generate embeddings
* Upload vectors to Pinecone

---

## Step 3 — Run Retrieval

```bash
python retriever.py
```

---

# Current Limitations

* Local file loaders only
* Sparse vector indexing not fully implemented
* No frontend/chat UI
* No persistent conversation memory
* No reranking pipeline yet

---

# Future Improvements

* Full Hybrid Retrieval (Dense + BM25)
* Sparse vector storage support
* Metadata filtering
* Reranking models
* Streaming responses
* Conversational memory
* Web UI integration
* Multi-modal document support

---

# Tech Stack

* Python
* LangChain
* Pinecone
* Hugging Face
* Sentence Transformers

---

# Use Case

This project is useful for:

* Internal knowledge base systems
* Enterprise document search
* AI assistants
* Semantic search pipelines
* Research document retrieval

---

# Status

🚧 Active Development — Retrieval pipeline functional, hybrid search under development.
