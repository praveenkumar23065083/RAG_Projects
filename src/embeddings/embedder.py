from sentence_transformers import SentenceTransformer


MODEL_NAME = "BAAI/bge-small-en-v1.5"


def load_embedding_model():
    model = SentenceTransformer(MODEL_NAME)
    return model


def generate_embeddings(model, texts):
    embeddings = model.encode(
        texts,
        normalize_embeddings=True
    )

    return embeddings