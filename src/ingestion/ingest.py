from src.ingestion.pdf_loader import load_pdf
from src.chunking.chunker import chunk_pages
from src.embeddings.embedder import (
    load_embedding_model,
    generate_embeddings
)
from src.vectorstore.chroma_store import create_chroma_collection


def ingest_pdf(pdf_path,document_name=None):

    # 1. Extract text from PDF
    pages = load_pdf(pdf_path)

    # 2. Create chunks
    chunks = chunk_pages(pages)

    if not chunks:
        raise ValueError("No usable text was found in the PDF.")

    # 3. Load embedding model
    model = load_embedding_model()

    # 4. Extract chunk texts
    texts = [chunk["text"] for chunk in chunks]

    # 5. Generate embeddings
    embeddings = generate_embeddings(
        model,
        texts
    )

    # 6. Get Chroma collection
    collection = create_chroma_collection()

    # 7. Prepare IDs and metadata
    ids = []
    metadatas = []

    for chunk in chunks:

        ids.append(
            f"{document_name or chunk['document_name']}_{chunk['chunk_id']}"
        )

        metadatas.append({
            "document_name": document_name or chunk["document_name"],
            "page_number": chunk["page_number"]
        })

    # 8. Store or update chunks in ChromaDB
    collection.upsert(
        ids=ids,
        embeddings=embeddings.tolist(),
        documents=texts,
        metadatas=metadatas
    )

    return len(chunks)