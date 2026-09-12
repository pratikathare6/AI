import os
from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain.agents import create_agent
from tools.tools import web_search,scrape_webpage

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
os.environ["GROQ_API_KEY"] = GROQ_API_KEY


llm = ChatGroq(model='openai/gpt-oss-120b')

#1st Agent search agent
def build_search_agent():
    return create_agent(

        model=llm,
        tools= [web_search],
         system_prompt="""You are a search agent summarize in 100 words.

TOOL: web_search
- Parameter: query (string) — REQUIRED
- Example: web_search(query="capital of india")

CRITICAL RULES:
1. ONLY use the 'query' parameter
2. NEVER use 'cursor', 'id', 'index', or any other parameter
3. Call it like: web_search(query="your search here")

DO NOT invent parameters. Only 'query' exists."""
        )

 #2nd Agent scraping agent 

def build_reader_agent():
    return create_agent(

        model=llm,
        tools= [scrape_webpage],
        system_prompt = """Reader agent. Use scrape_webpage on ONE URL. Summarize in 100 words.""")

writer_prompt = ChatPromptTemplate.from_messages([

    ("system","you are an expert reaserch writer. write clear,structured and insightful reports"),
    ("human",""" write a detailed report on the below topic 
     
     topic: {topic}

    reaserch gathered:
     {reaserch}

    structure the report as:
     
     - introduction
     - key findings (min 3 well explained points)
     - conclusion
     - sources (list all urls found in search)

     Be detailed factual and professional

""")
])


writer_chain = writer_prompt | llm | StrOutputParser()


critic_prompt = ChatPromptTemplate.from_messages([

    ("system","you are a sharp and constructive reaserch critic. Be honest and specific"),
    ("human", """ Review the research report below nad evaluate it strictly
     
     Report:
     {report}

     Respond in this exact format 

     Score: x/10

     Strengths:


     Areas to improve:

     one line verdict:

""")
])

critic_chain = critic_prompt | llm | StrOutputParser()


