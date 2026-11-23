from src.retrieval.vector_retriever import retrieve_chunks
from src.retrieval.bm25_retriever import retrieve_bm25

def retrieve_hybrid(
    query,
    top_k_vector=10,
    top_k_bm25=10,
    document_name=None
):

    vector_results = retrieve_chunks(
        query,
        top_k=top_k_vector,
        document_name=document_name
    )

    vector_chunks = []

    for i in range(len(vector_results["documents"][0])):

        vector_chunks.append({
            "id": vector_results["ids"][0][i],
            "text": vector_results["documents"][0][i],
            "document_name":
                vector_results["metadatas"][0][i]["document_name"],
            "page_number":
                vector_results["metadatas"][0][i]["page_number"]
        })

    bm25_chunks = retrieve_bm25(
        query,
        top_k=top_k_bm25,
        document_name=document_name
    )

    combined = {}

    for chunk in vector_chunks:
        combined[chunk["id"]] = chunk

    for chunk in bm25_chunks:
        combined[chunk["id"]] = chunk

    return list(combined.values())