from src.ingestion.pdf_loader import load_pdf
from src.chunking.chunker import chunk_pages

pdf_path="data/papers/Deepokan2.pdf"
pages=load_pdf(pdf_path)
chunks=chunk_pages(pages)

print("Number of pages:", len(pages))
print("Number of chunks:", len(chunks))

for chunk in chunks[:3]:
    print("\n--------------------")
    print("Document:", chunk["document_name"])
    print("Page:", chunk["page_number"])
    print("Chunk ID:", chunk["chunk_id"])
    print("Text:", chunk["text"])

