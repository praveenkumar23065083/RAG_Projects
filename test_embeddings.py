from src.ingestion.pdf_loader import load_pdf
from src.chunking.chunker import chunk_pages
from src.embeddings.embedder import load_embedding_model, generate_embeddings


# Load PDF
pdf_path = "data/papers/Deepokan2.pdf"

pages = load_pdf(pdf_path)

# Create chunks
chunks = chunk_pages(pages)

print("Number of pages:", len(pages))
print("Number of chunks:", len(chunks))


# Load embedding model
model = load_embedding_model()

print("Embedding model loaded.")


# Take first 3 chunks for testing
texts = [chunk["text"] for chunk in chunks[:3]]

# Generate embeddings
embeddings = generate_embeddings(model, texts)


print("Number of texts embedded:", len(texts))
print("Embedding shape:", embeddings.shape)

print("\nFirst embedding:")
print(embeddings[0])