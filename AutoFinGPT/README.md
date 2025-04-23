"""
# AutoFinGPT 🧠💰
*WARNING: I and this model are not financial advisors -- this is purely for experimentation and to showcase my skills and experience*

A fully local, open-source multi-agent AI system that ingests financial news, analyzes it using Retrieval-Augmented Generation (RAG), and simulates portfolio decision-making with Reinforcement Learning.
Gives some valuable insight but keep in mind this is local LLM, also the more data the better the results. If you would like to create a cron job in the background that constantly pulls RSS feeds it may help with accuracy.


## 🔧 Requirements
- Python 3.8+
- pip install -r requirements.txt

## 📦 Installation
```bash
git clone https://github.com/your-username/AutoFinGPT.git
cd AutoFinGPT
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
mkdir -p data/raw models
```

## 🚀 How to Run
```bash
python main.py
```
Follow the prompts to:
1. Scrape financial news from RSS feeds
2. Ask a question (e.g., "What sectors are bullish?")
3. See AI-generated insights using your local LLM

## 🧪 Optional: Train a PPO Agent
```bash
python rl_env/train_rl_agent.py
```
This will simulate trading over 100 timesteps and save the agent under `models/ppo_portfolio.zip`.

## 📁 Project Structure
- `agents/` — RAG + LLM agents
- `rag_pipeline/` — Embedding + vector search
- `rl_env/` — Gym environment + RL training
- `data/raw/` — Collected news data
- `models/` — Trained PPO models

## 🧠 Technologies
- SentenceTransformers
- FAISS
- Hugging Face Transformers and TinyLLama
- Stable-Baselines3 (PPO)

## 👨‍💻 Author
Ken Patel – [github.com/KPat11](https://github.com/KPat11)
