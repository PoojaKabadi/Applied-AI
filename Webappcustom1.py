import chromadb
import streamlit as st
from llama_index.core import PromptTemplate, Settings, SimpleDirectoryReader, StorageContext, VectorStoreIndex
from llama_index.core.node_parser import SentenceSplitter
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.llms.ollama import Ollama
from llama_index.vector_stores.chroma import ChromaVectorStore
from chromadb import PersistentClient
from llama_index.core.agent import ReActAgent
from llama_index.core.tools import FunctionTool
from duckduckgo_search import DDGS
import datetime


llm = None 
Settings.llm = Ollama(model="llama3.2", request_timeout=360.0)
embed_model = HuggingFaceEmbedding(model_name="BAAI/bge-small-en")
Settings.embed_model = embed_model


def multiply(a: int, b: int) -> int:
    """Multiply two integers and return the result"""
    return a * b

def add(a: int, b: int) -> int:
    """Add two integers and return the result"""
    return a + b

def subtract(a: int, b: int) -> int:
    """Subtract two integers and return the result"""
    return a - b

def search(query: str) -> str:
    """Search DuckDuckGo and return concatenated search results."""
    context = ""
    with DDGS() as req:
        response = req.text(query, max_results=3)
        for result in response:
            context += result.get('body', '')
    return context


def current_date() -> str:
    """Return today's date in a friendly format."""
    today = datetime.date.today()
    return today.strftime("%A, %B %d, %Y")  


search_tool = FunctionTool.from_defaults(fn=search)
multiply_tool = FunctionTool.from_defaults(fn=multiply)
add_tool = FunctionTool.from_defaults(fn=add)
subtract_tool = FunctionTool.from_defaults(fn=subtract)
date_tool = FunctionTool.from_defaults(fn=current_date)  


fntools = [multiply_tool, add_tool, subtract_tool, search_tool, date_tool]


agent = ReActAgent.from_tools(fntools, llm=Settings.llm, max_iterations=15, verbose=True)


st.title("🧠 AI-Powered Q&A Agent with Enhanced Features")
st.write("Welcome! Ask anything — math, search, or even today's date!")

user_query = st.text_input("Ask a question:", "")

if st.button("Submit"):
    if user_query:
        with st.spinner('Thinking...'):
            agent = ReActAgent.from_tools(fntools, llm=Settings.llm, max_iterations=15, verbose=True)
            answer = agent.chat(user_query)
            st.success('Done!')
            st.write("### Answer:", answer)
    else:
        st.warning("Please enter a question.")