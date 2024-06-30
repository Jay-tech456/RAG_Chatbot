## RAG Chatbot Using Haystack and Pinecone

This project is part of my portfolio, demonstrating my skills in building Retrieval-Augmented Generation (RAG) applications using different frameworks, vector databases, and techniques.

### Project Overview

This RAG application answers queries about recent news and financial reports related to Nvidia. The system combines several components to retrieve relevant information and generate accurate responses.

### Key Components

1. **Data Ingestion**: I used the Haystack framework to fetch documents from Nvidia news blogs. These documents were embedded and stored in the Pinecone vector database for efficient retrieval.

2. **Retrieval and Generation**: I integrated a prompt template with vectors retrieved from Pinecone and fed this data into the Mistral 7B model using the Hugging Face TGI Generator. This ensures high-quality, relevant responses.

3. **Application**: I developed a frontend application using Streamlit to provide a user-friendly interface for querying and displaying results.


Experimentation Questions tried with the RAG Chatbot:

Experimentation 1

<img width="944" alt="image" src="https://github.com/pavannagula/RAG-Application-Using-Mistral-and-Haystack/assets/39379433/1fe0d8da-196d-461c-9021-4d7da5c69236">



Experimentation 2

<img width="855" alt="image" src="https://github.com/pavannagula/RAG-Application-Using-Mistral-and-Haystack/assets/39379433/233001b9-a90e-49ec-8142-559efd296912">
