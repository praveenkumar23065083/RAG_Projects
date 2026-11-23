from src.retrieval.hybrid_retriever import retrieve_hybrid
from src.retrieval.reranker import rerank_chunks


query = "What is the difference between Transformers and DeepOKAN?"

# Get candidates from hybrid retrieval
chunks = retrieve_hybrid(
    query,
    top_k_vector=10,
    top_k_bm25=10
)

print("Hybrid candidates:", len(chunks))

# Rerank them
reranked_chunks = rerank_chunks(
    query,
    chunks,
    top_k=5
)

print("\n" + "=" * 80)
print("RERANKED RESULTS")
print("=" * 80)

for i, chunk in enumerate(reranked_chunks, start=1):

    print(f"\nRESULT {i}")
    print("Document:", chunk["document_name"])
    print("Page:", chunk["page_number"])
    print("Score:", chunk["rerank_score"])
    print("Text:", chunk["text"][:500])
    print("-" * 80)