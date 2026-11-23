from src.vectorstore.chroma_store import create_chroma_collection
from src.embeddings.embedder import load_embedding_model

def retrieve_chunks(query, top_k=5, document_name=None):

    model = load_embedding_model()

    query_embedding = model.encode(
        query,
        normalize_embeddings=True
    )

    collection = create_chroma_collection()

    where_filter = None

    if document_name:
        where_filter = {
            "document_name": document_name
        }

    results = collection.query(
        query_embeddings=[query_embedding.tolist()],
        n_results=top_k,
        where=where_filter
    )

    return results
