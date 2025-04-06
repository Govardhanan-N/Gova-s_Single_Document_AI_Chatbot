# rag_pipeline.py

from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import TextLoader, PyPDFLoader, Docx2txtLoader
from langchain_community.llms import Ollama
from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate
from langchain.retrievers import VectorStoreRetriever
import os

EMBEDDING_MODEL = "sentence-transformers/all-mpnet-base-v2"

def load_documents(path):
    try:
        if path.endswith(".pdf"):
            loader = PyPDFLoader(path)
        elif path.endswith(".docx"):
            loader = Docx2txtLoader(path)
        elif path.endswith(".txt"):
            loader = TextLoader(path)
        else:
            raise ValueError("Unsupported file type.  Please use .txt, .pdf, or .docx files.")
        return loader.load()
    except FileNotFoundError:
        raise FileNotFoundError(f"File not found: {path}")
    except Exception as e:
        raise RuntimeError(f"Error loading document: {e}")

def split_documents(documents):
    # TUNE THESE PARAMETERS FOR SINGLE DOCUMENT PRECISION
    splitter = RecursiveCharacterTextSplitter(chunk_size=400, chunk_overlap=40)  # Reduced chunk size
    return splitter.split_documents(documents)

def create_vector_store(docs, persist_directory="chroma_store"):
    if not docs:
        raise ValueError("No documents to embed. Make sure your input file has content.")

    embeddings = HuggingFaceEmbeddings(model_name=EMBEDDING_MODEL)

    try:
        vectordb = Chroma.from_documents(
            documents=docs,
            embedding=embeddings,
            persist_directory=persist_directory
        )
        vectordb.persist()
        return vectordb
    except ValueError as e:
        raise ValueError("Vector embedding failed. Ensure text chunks are valid and non-empty.") from e
    except Exception as e:
        raise RuntimeError(f"Error creating vector store: {e}") from e

def load_qa_chain(persist_directory="chroma_store"):
    embeddings = HuggingFaceEmbeddings(model_name=EMBEDDING_MODEL)
    vectordb = Chroma(persist_directory=persist_directory, embedding_function=embeddings)

    # TUNE THESE PARAMETERS FOR SINGLE DOCUMENT PRECISION
    retriever = VectorStoreRetriever(vectorstore=vectordb, search_kwargs={"k": 4})  # Reduced k

    llm = Ollama(model="mistral", base_url="http://localhost:11434")

    prompt_template = """You are a helpful assistant providing information *only* from the provided document.
    *DO NOT* use outside information. If the answer isn't explicitly stated, say you don't know.

    Answer questions accurately and concisely. Aim for structured output where possible.

    Document Context:
    {context}

    Question: {question}

    Answer:
    """
    PROMPT = PromptTemplate(
        template=prompt_template, input_variables=["context", "question"]
    )

    chain_type_kwargs = {"prompt": PROMPT}

    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=retriever,
        chain_type_kwargs=chain_type_kwargs,
        return_source_documents=True
    )
    return qa_chain