# We will put encoded data into our open source db faiss
import faiss
import numpy as np

#creating faiss index using Euclidean distance to map for similarities among vectors
def create_faiss_index(embeddings):
    index = faiss.IndexFlatL2(len(embeddings[0]))
    index.add(np.array(embeddings))
    return index

#this function will help find the k nearest vectors and indices, we will then return them for query handler to find the data with those mappings
def search(query_vec, index, k=5):
    _, I = index.search(np.array([query_vec]), k)
    return I[0]