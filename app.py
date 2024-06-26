from fastapi import FastAPI, Request, Form, Response
from fastapi.templating import Jinja2Templates
from fastapi.encoders import jsonable_encoder
import uvicorn
from fastapi import FastAPI
import json
import os
from dotenv import load_dotenv
from Chatbot_system.RetrievalandGeneration import get_result

#loading the environment variable
load_dotenv()
PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
print("API Key Imported Successfully")

#creating the app
app = FastAPI()

# Configure templates
templates = Jinja2Templates(directory="Templates")

#creating the routes with bind functions
@app.get("/")
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})
    
@app.post("/get_answer")
async def get_answer(request: Request, question: str = Form()):
    print(question)
    answer= get_result(question)
    response_data = jsonable_encoder(json.dumps({"answer": answer}))
    res = Response(response_data)
    return res
    
if __name__ == "__main__":
    uvicorn.run("app:app",host="0.0.0.0",port=8000,reload=True)