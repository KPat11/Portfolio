# AutoFinGPT 🚀

A multi-agent AI system that scrapes real-time financial news, performs RAG-based analysis, and adjusts a simulated investment portfolio using reinforcement learning.

## 🔧 Tech Stack
- RAG: LlamaIndex / Haystack
- LLM: Mixtral, LLaMA2
- Vector DB: FAISS / ChromaDB
- RL: Stable-Baselines3
- Data: Yahoo Finance, scraped news

## 💡 Features
- Agent-based scraping, analysis, and decision-making
- Custom RL environment for finance
- Retrieval-augmented language understanding
- Fully offline, free-to-run simulation

## 🗂️ Project Structure
- `/agents` – LLM and RL agents
- `/rag_pipeline` – Vector search + context retrieval
- `/rl_env` – Gym environment for trading decisions
- `/data` – Includes synthetic and real scraped data

## 🛠️ Setup

```bash
cd AutoFinGPT
pip install -r requirements.txt
