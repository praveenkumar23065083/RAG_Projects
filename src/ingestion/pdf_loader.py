import pymupdf
from pathlib import Path


def load_pdf(pdf_path):
    document=pymupdf.open(pdf_path)
    document_name=Path(pdf_path).name
    pages=[]
    for page_number, page in enumerate(document,start=1):
        text=page.get_text()
        pages.append({
            "document_name":document_name,
            "page_number":page_number,
            "text":text
        })
    document.close()
    return pages


#TESTING CODE
'''
if __name__=="__main__":
    pdf_path="data/papers/Deepokan2.pdf"
    pages=load_pdf(pdf_path)
    print(f"Number of pages: {len(pages)}")
    for page in pages:
        print(f"\n--- Page {page['page_number']} ---")
        print(page["text"][:500])
'''
