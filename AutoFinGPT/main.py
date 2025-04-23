# 📁 AutoFinGPT – Full Local Open-Source Project

from agents.news_retriever import scrape_rss
from rag_pipeline.query_handler import semantic_search
from agents.summarizer_llm import genereate_summary

if __name__ == "__main__":
    print("\n🚀 AutoFinGPT: Multi-Agent Financial Intelligence System\n")

    # Step 1: Fetch latest headlines
    print("📥 Scraping RSS headlines...")
    scrape_rss()

    #Step 2: Perform semantic search
    query = input("\n🔍 What financial question would you like to ask?\n> ")
    print("\n📊 Retrieving relevant news...")
    headlines = semantic_search(query)

    #Step 3: Summarize with LLM
    print("\n🧠 Generating insight with local LLM...")
    summary = genereate_summary(headlines, user_instruction=f"Answer this question using financial the financial data gathered: {query}")
    print("\n📝 Summary:\n")
    print(summary)