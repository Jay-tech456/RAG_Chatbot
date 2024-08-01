from haystack_integrations.document_stores.pinecone import PineconeDocumentStore
import os
from dotenv import load_dotenv

def pinecone_config():
    load_dotenv()
    PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")

    #print("Pinecone API key is Imported Successfully")
    # Configure Pinecone database
    document_store = PineconeDocumentStore(
        index="rag-chatbot-meta-rl",
        metric="cosine",
        dimension=768
    )
    return document_store

