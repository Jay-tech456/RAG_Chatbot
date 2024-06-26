from haystack import Pipeline
from haystack.components.writers import DocumentWriter
from haystack.components.preprocessors import DocumentSplitter
from haystack.components.embedders import SentenceTransformersDocumentEmbedder
from haystack_integrations.document_stores.pinecone import PineconeDocumentStore
from haystack.components.converters import PyPDFToDocument
from pathlib import Path 
import os
from dotenv import load_dotenv
from Chatbot_system.utils import pinecone_config

load_dotenv
file_path = os.getenv('FILE_PATH')
def data_ingest(document_store):
    
    indexing = Pipeline()

    # Adding the components to the pipeline
    indexing.add_component("Document_converter", PyPDFToDocument())
    indexing.add_component("Document_splitter", DocumentSplitter(split_by="sentence", split_length=2))
    indexing.add_component("Document_Embedding", SentenceTransformersDocumentEmbedder())
    indexing.add_component("Document_Writer", DocumentWriter(document_store))
    
    # Connecting all the components of pipeline
    indexing.connect("Document_converter", "Document_splitter")
    indexing.connect("Document_splitter", "Document_Embedding")
    indexing.connect("Document_Embedding", "Document_Writer")

    # Store the data as vector embeddings into the dataset folder
    indexing.run({"Document_converter": {"sources": [Path(file_path)]}})


if __name__ == "__main__":
    
    os.environ['Pinecone_API_KEY'] = os.getenv('Pinecone_API_KEY')

    document_store = pinecone_config()

    data_ingest(document_store)
