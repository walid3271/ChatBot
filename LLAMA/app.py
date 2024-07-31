from fastapi import FastAPI
from langchain.prompts import ChatPromptTemplate
from langserve import add_routes
import uvicorn
from langchain_community.llms import Ollama
from dotenv import load_dotenv

load_dotenv()
app=FastAPI(title="Langchain Server", version="1.0", decsription="A simple API Server")
llm=Ollama(model="llama2")
prompt=ChatPromptTemplate.from_template("Write me about {topic} with 200 words")
add_routes(app, prompt|llm, path="/ask")

if __name__=="__main__":
    uvicorn.run(app,host="localhost",port=8000)
    
# python -m uvicorn app:app --reload