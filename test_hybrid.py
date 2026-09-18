from src.retrieval.hybrid_retriever import retrieve_hybrid


query = "What is the difference between Transformers and DeepOKAN?"

results = retrieve_hybrid(
    query,
    top_k_vector=10,
    top_k_bm25=10
)

print("\nNumber of retrieved chunks:", len(results))

print("\n" + "=" * 80)

for i, chunk in enumerate(results, start=1):

    print(f"\nRESULT {i}")
    print("Document:", chunk["document_name"])
    print("Page:", chunk["page_number"])
    print("Text:")
    print(chunk["text"][:500])
    print("-" * 80)