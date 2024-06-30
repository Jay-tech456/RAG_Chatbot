from haystack.utils import Secret
from haystack.components.embedders import SentenceTransformersTextEmbedder
from haystack.components.builders import PromptBuilder
from haystack_integrations.components.retrievers.pinecone import PineconeEmbeddingRetriever
from haystack.components.generators import HuggingFaceTGIGenerator
from haystack import Pipeline
from Chatbot_system.data_ingestion import data_ingest
from Chatbot_system.utils import pinecone_config
import os
from dotenv import load_dotenv

prompt_template = """
You are a helpful AI assistant. Your task is to answer the query based on the provided context. Follow these guidelines:

1. Use only the information from the given documents to answer the query.
2. If the answer is not explicitly stated in the documents, respond with "I don't have enough information to answer this question."
3. If the documents contain conflicting information, mention the discrepancy in your answer.
4. Provide a detailed explanation of answer with accurate information, citing the relevant document(s) when possible.

Query: {{query}}

Context:
{% for doc in documents %}
Document {{loop.index}}:
{{doc.content}}

{% endfor %}

Answer: 
"""

def get_result(query):                  
    query_pipeline = Pipeline()

    query_pipeline.add_component("text_embedder", SentenceTransformersTextEmbedder())
    query_pipeline.add_component("retriever", PineconeEmbeddingRetriever(document_store=pinecone_config()))
    query_pipeline.add_component("prompt_builder", PromptBuilder(template=prompt_template))
    query_pipeline.add_component("generator", HuggingFaceTGIGenerator(model="mistralai/Mistral-7B-v0.1", token = Secret.from_env_var("HF_API_TOKEN")))

    query_pipeline.connect("text_embedder.embedding", "retriever.query_embedding")
    query_pipeline.connect("retriever.documents", "prompt_builder.documents")
    query_pipeline.connect("prompt_builder", "generator")

    query = query

    results = query_pipeline.run(
        {
            "text_embedder": {"text": query},
            "prompt_builder": {"query": query},
        }
    )

    return results['generator']['replies'][0]


if __name__ == '__main__':
    
    result=get_result("Can you explain me how to Fine-Tuning With NeMo, Optimizing for Inference With TensorRT-LLM?")
    print(result)