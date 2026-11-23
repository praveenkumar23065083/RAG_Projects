from rank_bm25 import BM25Okapi
from src.vectorstore.chroma_store import create_chroma_collection

def retrieve_bm25(query, top_k=5, document_name=None):

    collection = create_chroma_collection()

    where_filter = None

    if document_name:
        where_filter = {
            "document_name": document_name
        }

    data = collection.get(
        where=where_filter
    )

    documents = data["documents"]
    metadatas = data["metadatas"]
    ids = data["ids"]

    if not documents:
        return []

    tokenized_documents = [
        document.lower().split()
        for document in documents
    ]

    bm25 = BM25Okapi(tokenized_documents)

    tokenized_query = query.lower().split()

    scores = bm25.get_scores(tokenized_query)

    ranked_indices = sorted(
        range(len(scores)),
        key=lambda i: scores[i],
        reverse=True
    )

    results = []

    for index in ranked_indices[:top_k]:

        results.append({
            "id": ids[index],
            "text": documents[index],
            "document_name": metadatas[index]["document_name"],
            "page_number": metadatas[index]["page_number"],
            "score": float(scores[index])
        })

    return results
