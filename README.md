<h1 align="center">Applied AI Capstone: Building a Local Agentic AI System</h1>
<p align="center">
  <a href="https://github.com/PoojaKabadi/Applied-AI/tree/main">
    <img src="https://github.com/user-attachments/assets/3fa79dd8-850e-462b-bd33-807f54594308" alt="Applied AI" width="900px" />
  </a>
  <br><i>
   Built a modular, locally hosted AI agent capable of multi-step reasoning and autonomous tool use, deployed via a Streamlit web interface using LlamaIndex, Ollama, and ChromaDB.
  </p>

### Description:
This capstone project focused on building an intelligent Agentic AI system capable of autonomous reasoning and decision-making using local LLMs. By leveraging the ReAct architecture, the system simulates thought–observation–action loops to answer complex user queries using both logic functions and web search tools.

The agent was integrated into a Streamlit web app and augmented with additional features like date retrieval and error handling. Additionally, a custom RAG (Retrieval-Augmented Generation) pipeline was developed using LlamaIndex, embedding models from HuggingFace, and persistent vector storage with ChromaDB.

#### Key highlights include:

- Implemented a ReAct agent that chains together tools like add, multiply, and DuckDuckGo Search using FunctionTool
- Hosted and queried open-source LLMs like Llama3.2 and Phi3-Mini using Ollama locally
- Built a local RAG pipeline that loads documents, splits them into semantic chunks, indexes them, and retrieves relevant context dynamically
- Created an interactive Streamlit frontend for natural language Q&A with memory and dynamic agent routing
- Experimented with prompt tuning, Top-K, Top-P, and temperature settings to optimize output quality

This project highlights hands-on experience in deploying autonomous AI agents, integrating open-source AI models, and bridging backend logic with a user-facing app.

📅 Timeline: April–May 2025

📦 Tools Used: Python, LlamaIndex, Ollama, Streamlit, ChromaDB, DuckDuckGo Search, HuggingFace Embeddings
