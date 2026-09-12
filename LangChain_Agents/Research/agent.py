import os
import streamlit as st
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_community.tools.tavily_search import TavilySearchResults
from langchain.agents import create_agent
from langchain_core.messages import HumanMessage
import requests
from langchain.tools import tool

load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")
WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")


# Search tool
search_tool = TavilySearchResults(max_results=3)

# LLM
llm = ChatGroq(api_key=GROQ_API_KEY, model='openai/gpt-oss-20b')

# Weather tool
@tool
def get_weather_data_tool(city: str) -> str:
    """Fetch current weather for a city"""
    url = f'http://api.weatherstack.com/current?access_key={WEATHER_API_KEY}&query={city}'
    response = requests.get(url)
    data = response.json()
    return data

tools = [search_tool, get_weather_data_tool]

# Create agent
weather_agent = create_agent(
    model=llm,
    tools=tools,
    system_prompt='You are a weather expert assistant.'
)

# ======================================
# Streamlit UI
# ======================================

st.set_page_config(page_title="Weather Agent", page_icon="🌤️")

st.title("🌤️ Weather Agent")
st.write("Ask me about any city's weather!")

# User input
user_question = st.text_input("Enter your question:", placeholder="e.g., Find the capital of India and tell me its weather")

if st.button("Get Weather"):
    if user_question:
        with st.spinner("Thinking..."):
            try:
                 
                response = weather_agent.invoke(
                    {"messages": [HumanMessage(content=user_question)]}
                )
                
                # Display result
                st.success("✅ Here's your answer:")
                st.write(response['messages'][-1].content)
                
            except Exception as e:
                st.error(f"Error: {e}")
    else:
        st.warning("Please enter a question!")