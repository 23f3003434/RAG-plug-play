# Simple Plug & Play RAG

This project has focused on **Data Chunking and Data Retrieval** rather than frontend and conversational chatbot(prompt eng and conversation history management) 




## Data Loading
* Currently only supports local files, due to testing unavailability with other loader apis
* Create a folder named data inside which create sub folders [pdf,csv,text] place corresponding files
* Every run loads the data into langchain document type 
* For testing complete merged data is saved as json 


## Data Chunking 

* Subfolders are automatically created for each file type and file name
* Tune internal parameters as per your choice in data_fetch.py for chunk size 


## LLM Instance 




