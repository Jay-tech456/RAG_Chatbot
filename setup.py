from setuptools import find_packages, setup

setup(
    name="RAG Chatbot System using Mistral and Haystack",
    version="0.0.1",
    author="pavannagula",
    author_email="pavannagula76@gmail.com",
    packages=find_packages(),
    install_requires=["pinecone-haystack","haystack-ai","fastapi","uvicorn","python-dotenv","pathlib"]
)