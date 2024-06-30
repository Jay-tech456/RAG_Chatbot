import requests
import streamlit as st
from dotenv import load_dotenv
from Chatbot_system.RetrievalandGeneration import get_result

# Title
st.set_page_config(page_title="RAG Chatbot Using Haystack Mistral & Pinecone", layout="wide")
st.title("RAG With Haystack Mistral & Pinecone")

# Input Form
with st.form(key="query_form"):
    question = st.text_area("Ask Anything!", height=150)
    submit_button = st.form_submit_button(label="Submit")

# Output section for the answer
answer_placeholder = st.empty()
info_placeholder = st.empty()

# Processing the Form Submission
if submit_button:
    if not question:
        st.error("Please enter your query!")
    else:
        info_placeholder.info("Processing your query... Please wait.")
        try:
            answer = get_result(question)
            answer_placeholder.text_area("Answer", value=answer, height=150, disabled=True)
            info_placeholder.empty()  
        except Exception as e:
            info_placeholder.empty()  
            st.error(f"An error occurred: {e}")

# CSS styling
st.markdown(
    """
    <style>
    .stTextArea {
        font-family: 'Fira Code', monospace;
        background-color: #f8f9fa !important;
        color: #495057 !important;
    }
    .stButton button {
        background-color: #007bff !important;
        color: #ffffff !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)