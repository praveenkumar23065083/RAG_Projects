from sentence_transformers import CrossEncoder


MODEL_NAME = "cross-encoder/ms-marco-MiniLM-L-6-v2"


def load_reranker():

    model = CrossEncoder(MODEL_NAME)

    return model


def rerank_chunks(
    query,
    chunks,
    top_k=5
):

    if not chunks:
        return []

    model = load_reranker()

    pairs = [
        [query, chunk["text"]]
        for chunk in chunks
    ]

    scores = model.predict(pairs)

    ranked_chunks = []

    for chunk, score in zip(chunks, scores):

        chunk = chunk.copy()

        chunk["rerank_score"] = float(score)

        ranked_chunks.append(chunk)

    ranked_chunks.sort(
        key=lambda x: x["rerank_score"],
        reverse=True
    )

    return ranked_chunks[:top_k]