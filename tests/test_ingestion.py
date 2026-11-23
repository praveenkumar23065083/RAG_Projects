from src.ingestion.ingest import ingest_pdf
pdf_path = "data/papers/Deepokan2.pdf"

number_of_chunks = ingest_pdf(pdf_path)

print("PDF successfully ingested.")
print("Chunks added or updated:", number_of_chunks)