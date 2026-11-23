def chunk_pages(pages, chunk_size=1500, overlap=200):
    chunks = []

    for page in pages:
        text = page["text"].strip()

        if not text:
            continue

        paragraphs = [p.strip() for p in text.split("\n\n") if p.strip()]

        current_chunk = ""
        chunk_number = 0

        for paragraph in paragraphs:

            # If a single paragraph itself is larger than the chunk size,
            # split it into smaller pieces.
            if len(paragraph) > chunk_size:

                if current_chunk.strip():
                    chunks.append({
                        "document_name": page["document_name"],
                        "page_number": page["page_number"],
                        "chunk_id": f"p{page['page_number']}_c{chunk_number}",
                        "text": current_chunk.strip()
                    })

                    chunk_number += 1
                    current_chunk = ""

                start = 0

                while start < len(paragraph):
                    end = start + chunk_size
                    piece = paragraph[start:end].strip()

                    if piece:
                        chunks.append({
                            "document_name": page["document_name"],
                            "page_number": page["page_number"],
                            "chunk_id": f"p{page['page_number']}_c{chunk_number}",
                            "text": piece
                        })

                        chunk_number += 1

                    start = end - overlap

                continue

            # Normal case: add paragraph to current chunk
            if len(current_chunk) + len(paragraph) + 2 <= chunk_size:
                current_chunk += paragraph + "\n\n"

            else:
                if current_chunk.strip():
                    chunks.append({
                        "document_name": page["document_name"],
                        "page_number": page["page_number"],
                        "chunk_id": f"p{page['page_number']}_c{chunk_number}",
                        "text": current_chunk.strip()
                    })

                    chunk_number += 1

                overlap_text = current_chunk[-overlap:].strip()

                current_chunk = overlap_text + "\n\n" + paragraph

        # Save remaining text
        if current_chunk.strip():
            chunks.append({
                "document_name": page["document_name"],
                "page_number": page["page_number"],
                "chunk_id": f"p{page['page_number']}_c{chunk_number}",
                "text": current_chunk.strip()
            })

    return chunks