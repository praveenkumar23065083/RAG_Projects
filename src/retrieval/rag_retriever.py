from src.retrieval.hybrid_retriever import retrieve_hybrid
from src.retrieval.reranker import rerank_chunks


def retrieve_relevant_chunks(
    query,
    document_name=None,
    top_k_vector=10,
    top_k_bm25=10,
    top_k_final=5
):

    candidates = retrieve_hybrid(
        query,
        top_k_vector=top_k_vector,
        top_k_bm25=top_k_bm25,
        document_name=document_name
    )

    print("\n" + "=" * 80)
    print("HYBRID CANDIDATES")
    print("=" * 80)

    for i, chunk in enumerate(candidates, 1):
        print(
            i,
            chunk["document_name"],
            "Page:", chunk["page_number"]
        )

    reranked = rerank_chunks(
        query,
        candidates,
        top_k=len(candidates)
    )

    print("\n" + "=" * 80)
    print("RERANKED CANDIDATES")
    print("=" * 80)

    for i, chunk in enumerate(reranked, 1):
        print(
            i,
            chunk["document_name"],
            "Page:", chunk["page_number"],
            "Score:", chunk["rerank_score"]
        )

    return reranked[:top_k_final]