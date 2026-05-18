import faiss
import numpy as np

index = faiss.IndexFlatL2(384)
document_store = []


def store_embeddings(embeddings, chunks):
    global document_store

    embeddings = np.array(embeddings).astype('float32')
    index.add(embeddings)

    document_store.extend(chunks)


def search_embeddings(query_embedding, top_k=3):
    query_embedding = np.array([query_embedding]).astype('float32')

    distances, indices = index.search(query_embedding, top_k)

    results = []

    for idx in indices[0]:
        if idx < len(document_store):
            results.append(document_store[idx])

    return results