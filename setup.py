from setuptools import find_packages, setup

setup(
    name="RAG Chatbot System using Mistral and Haystack",
    version="0.0.1",
    author="xxxxx",
    author_email="xxxxx",
    packages=find_packages(),
    install_requires=["pinecone-haystack","haystack-ai","python-dotenv","pathlib"]
)