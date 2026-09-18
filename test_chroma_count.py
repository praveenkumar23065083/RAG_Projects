from src.vectorstore.chroma_store import create_chroma_collection
collection = create_chroma_collection()
print("Total chunks in ChromaDB:", collection.count())