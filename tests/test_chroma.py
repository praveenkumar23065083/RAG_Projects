from src.ingestion.pdf_loader import load_pdf
from src.chunking.chunker import chunk_pages
from src.embeddings.embedder import (
    load_embedding_model,
    generate_embeddings
)
from src.vectorstore.chroma_store import create_chroma_collection


# --------------------------------------------------
# 1. Load PDF
# --------------------------------------------------

pdf_path = "data/papers/Deepokan2.pdf"

pages = load_pdf(pdf_path)

print("Number of pages:", len(pages))


# --------------------------------------------------
# 2. Create chunks
# --------------------------------------------------

chunks = chunk_pages(pages)

print("Number of chunks:", len(chunks))


# --------------------------------------------------
# 3. Load embedding model
# --------------------------------------------------

model = load_embedding_model()

print("Embedding model loaded.")


# --------------------------------------------------
# 4. Generate embeddings
# --------------------------------------------------

texts = [chunk["text"] for chunk in chunks]

embeddings = generate_embeddings(model, texts)

print("Embeddings generated.")
print("Embedding shape:", embeddings.shape)


# --------------------------------------------------
# 5. Create Chroma collection
# --------------------------------------------------

collection = create_chroma_collection()

print("Chroma collection created.")


# --------------------------------------------------
# 6. Add chunks to Chroma
# --------------------------------------------------

ids = []
metadatas = []

for chunk in chunks:

    ids.append(chunk["chunk_id"])

    metadatas.append({
        "document_name": chunk["document_name"],
        "page_number": chunk["page_number"]
    })


collection.add(
    ids=ids,
    embeddings=embeddings.tolist(),
    documents=texts,
    metadatas=metadatas
)


print("Chunks added to ChromaDB.")
print("Total items in database:", collection.count())