import chromadb
def create_chroma_collection():

    client = chromadb.PersistentClient(
        path="chroma_db"
    )

    collection = client.get_or_create_collection(
        name="paperlens"
    )

    return collection