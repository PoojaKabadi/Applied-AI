import chromadb
from llama_index.core import PromptTemplate, Settings, SimpleDirectoryReader,StorageContext, VectorStoreIndex
from llama_index.core.node_parser import SentenceSplitter
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.llms.ollama import Ollama
from llama_index.vector_stores.chroma import ChromaVectorStore
from chromadb import PersistentClient
from llama_index.core.agent import ReActAgent
from llama_index.core.tools import FunctionTool
from duckduckgo_search import DDGS


llm =None 
Settings.llm=Ollama(model="llama3.2", request_timeout=360.0)
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
    """
    Args:
        query (str): User's search prompt.

    Returns:
        context (str): Combined search results from DuckDuckGo.
    """
    context = ""
    with DDGS() as req:
        response = req.text(query, max_results=3)
        for result in response:
            context += result.get('body', '')  # Safe get to avoid KeyError

    return context

search_tool = FunctionTool.from_defaults(fn=search)
multiply_tool=FunctionTool.from_defaults(fn=multiply)
add_tool=FunctionTool.from_defaults(fn=add)
subtract_tool=FunctionTool.from_defaults(fn=subtract)

fntools = [multiply_tool, add_tool,subtract_tool,search_tool]

agent = ReActAgent.from_tools(fntools, llm=Settings.llm,
max_iterations=15,verbose=True)

response=agent.chat("Who is Cristiano Ronaldo and what is his current age multiplied by 2?")

print(response)








