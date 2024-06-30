# RAG Chatbot Using Haystack and Pinecone

I have done this project as a collection to my portfolio to cover my expertise in building RAG applications using various frameworks, vector databases, and techniques.

This project is about answering queries related recent news about Nvidia's news and financial reports. 
  1. Data Ingestion: I have used haystack framework for fetching the documents from the Nvidia news blogs and embedded and stored them into the pinecone vector database.
  2. Retrival and Generation: I have integrated the prompt template with pinecone retrived vectors and feeded that into the Mistral 7B model using HuggingFaceTGIGenerator
  3. Application: Finaly, Used the streamlit for the frontend application and generated the results.

 Example questions tried with the RAG Chatbot:
 
