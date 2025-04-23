# With the goal of being completely open source, I will be using Hugging Face's transformers to vectorize our news feed

from sentence_transformers import SentenceTransformer

# using model all-MiniLM-L6-v2
model = SentenceTransformer('all-MiniLM-L6-v2')

def get_embeddings(texts):
    return model.encode(texts)

def embed_query(text):
    return model.encode([text])[0] #accounted for only wanted 1 vector not a list of vectors
