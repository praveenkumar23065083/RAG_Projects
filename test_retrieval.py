from src.retrieval.vector_retriever import retrieve_chunks


query = "What is DeepOKAN and what is the main idea behind it?"

results = retrieve_chunks(query, top_k=5)


print("\nQuery:")
print(query)

print("\nRetrieved chunks:")

for i in range(len(results["documents"][0])):

    print("\n" + "=" * 80)

    print("Rank:", i + 1)

    print("Distance:", results["distances"][0][i])

    print("Document:", results["metadatas"][0][i]["document_name"])

    print("Page:", results["metadatas"][0][i]["page_number"])

    print("\nText:")
    print(results["documents"][0][i])