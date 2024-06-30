from haystack import Pipeline
from haystack.components.converters import HTMLToDocument
from haystack.components.writers import DocumentWriter
from haystack.components.preprocessors import DocumentSplitter
from haystack.components.fetchers import LinkContentFetcher
from haystack.components.embedders import SentenceTransformersDocumentEmbedder
from haystack_integrations.document_stores.pinecone import PineconeDocumentStore
from haystack.components.converters import PyPDFToDocument
from pathlib import Path 
import os
from dotenv import load_dotenv
from Chatbot_system.utils import pinecone_config


def data_ingest(document_store):
    
    indexing = Pipeline()

    # Adding the components to the pipeline
    indexing.add_component("Document_fetcher", LinkContentFetcher())
    indexing.add_component("Document_converter", HTMLToDocument())
    indexing.add_component("Document_splitter", DocumentSplitter(split_by="sentence", split_length=2))
    indexing.add_component("Document_Embedding", SentenceTransformersDocumentEmbedder())
    indexing.add_component("Document_Writer", DocumentWriter(document_store))
    
    # Connecting all the components of pipeline
    indexing.connect("Document_fetcher", "Document_converter")
    indexing.connect("Document_converter", "Document_splitter")
    indexing.connect("Document_splitter", "Document_Embedding")
    indexing.connect("Document_Embedding", "Document_Writer")

    urls = ["https://blogs.nvidia.com/blog/nemotron-4-synthetic-data-generation-llm-training/"]

    indexing.run({"Document_fetcher": {"urls": urls}})

if __name__ == "__main__":
    
    document_store=pinecone_config()
    data_ingest(document_store)
