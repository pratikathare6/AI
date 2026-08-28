import os 
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_groq import ChatGroq
from dotenv import load_dotenv,find_dotenv
from fastapi import FastAPI
from langserve import add_routes
import uvicorn

_=load_dotenv(find_dotenv())
groq_api_key = os.environ["GROQ_API_KEY"]

llm = ChatGroq(model='openai/gpt-oss-20b')

parser  = StrOutputParser()

system_prompt = "Translate the following into {language}"

prompt_template = ChatPromptTemplate.from_messages([

    ('system',system_prompt),
    ('user','{text}')
])

chain = prompt_template | llm | parser

app = FastAPI(

    title= 'SimpleTranslator',
    version='1.o',
    description="A simple API server using Langchain's runnable interfaces"
)

add_routes(app,
           chain,
           path="/chain"
           )

if __name__ == "__main__":
    uvicorn.run(app,host="localhost",port=8080)
    