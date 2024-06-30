import requests
import streamlit as st
from dotenv import load_dotenv
from src.generation import get_result

# Title
st.set_page_config(page_title="RAG Chatbot Using Haystack Mistral & Pinecone", layout="wide")
st.title("RAG With Haystack Mistral & Pinecone")


# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Accept user input
if prompt := st.chat_input("Ask me anything!"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)

    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        user_prompt = st.session_state.messages[-1]["content"]
        
        answer = get_result(user_prompt)
        response = st.write(answer)
    st.session_state.messages.append({"role": "assistant", "content": answer})