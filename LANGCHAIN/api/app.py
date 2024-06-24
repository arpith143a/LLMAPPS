from fastapi import FastAPI
from langchain.prompts import ChatPromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain_google_vertexai import ChatVertexAI
from langserve import add_routes
import uvicorn
import os
from langchain_community.llms import Ollama
from dotenv import load_dotenv

load_dotenv()

os.environ['OPENAI_API_KEY']=os.getenv("OPENAI_API_KEY")
os.environ['GOOGLE_API_KEY']=os.getenv("GOOGLE_API_KEY")

app=FastAPI(
    title="Langchain Server",
    version="1.0",
    decsription="A simple API Server"

)

add_routes(
    app,
    ChatOpenAI(),
    path="/openai"
)

model=ChatOpenAI()
llm=Ollama(model='llama2')
google=ChatVertexAI(model="gemini-pro")

prompt1=ChatPromptTemplate.from_template(
    "write me an essay about {topic} with 200 words"
)

prompt2=ChatPromptTemplate.from_template(
    "write me an poem about {topic} with 200 words"
)

prompt2=ChatPromptTemplate.from_template(
    "write me an summary about {topic} with 50 words"
)

add_routes(
    app,
    prompt1|model,
    path="/essay"
)

add_routes(
    app,
    prompt2|llm,
    path="/poem"
)

add_routes(
    app,
    prompt3|google,
    path="/summary"
)

if __name__=="__main__":
    uvicorn.run(app,host="localhost",port=8000)
