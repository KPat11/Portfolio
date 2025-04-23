#goal is to handle k nearest indices to obtain data at those vectors
import pandas as pd
from rag_pipeline.embedder import embed_query, get_embeddings
from rag_pipeline.vector_db import create_faiss_index, search 

def semantic_search(query):
    df = pd.read_csv("data/raw/news.csv")
    docs = df["title"].tolist()
    embeddings = get_embeddings(docs) #from our embedding.py
    index = create_faiss_index(embeddings)
    query_vec = embed_query(query)
    indices = search(query_vec, index)
    return [docs[i] for i in indices]