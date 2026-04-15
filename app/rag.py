from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

model = SentenceTransformer("all-MiniLM-L6-v2")

def split_text(text, size=200):
    return [text[i:i+size] for i in range(0, len(text), size)]

def build_index(text):
    chunks = split_text(text)
    embeddings = model.encode(chunks)

    index = faiss.IndexFlatL2(embeddings.shape[1])
    index.add(np.array(embeddings))

    return index, chunks

def retrieve(query, index, chunks, k=2):
    q_emb = model.encode([query])
    D, I = index.search(np.array(q_emb), k)

    return [chunks[i] for i in I[0]]