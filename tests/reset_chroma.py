import chromadb
client = chromadb.PersistentClient(
    path="chroma_db"
)

try:

    client.delete_collection(
        name="paperlens"
    )

    print(
        "Chroma collection deleted successfully."
    )

except Exception as e:

    print(
        "Could not delete collection:"
    )

    print(e)