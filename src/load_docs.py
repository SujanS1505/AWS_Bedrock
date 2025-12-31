from langchain_community.document_loaders import PyPDFLoader, TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
import os

def load_documents():
    docs = []


    pdf_path = "data/pdfs"
    for file in os.listdir(pdf_path):
        if file.endswith(".pdf"):
            loader = PyPDFLoader(os.path.join(pdf_path, file))
            docs.extend(loader.load())


    txt_path = "data/texts"
    for file in os.listdir(txt_path):
        if file.endswith(".txt"):
            loader = TextLoader(os.path.join(txt_path, file))
            docs.extend(loader.load())


    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=100
    )

    return splitter.split_documents(docs)
