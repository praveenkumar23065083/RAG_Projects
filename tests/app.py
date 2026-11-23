import streamlit as st

import tempfile
import os

from src.ingestion.ingest import ingest_pdf
from src.vectorstore.chroma_store import create_chroma_collection
from src.retrieval.hybrid_retriever import retrieve_hybrid
from src.generation.generator import generate_answer

st.set_page_config(
    page_title="PaperLens",
    page_icon="📄",
    layout="wide"
)


st.title("📄 PaperLens")

st.caption(
    "Research Paper RAG Assistant"
)


# ==========================================================
# SIDEBAR
# ==========================================================

st.sidebar.header(
    "Upload Research Papers"
)


uploaded_file = st.sidebar.file_uploader(
    "Upload a PDF",
    type=["pdf"]
)


if uploaded_file is not None:

    if st.sidebar.button("Process PDF"):

        with tempfile.NamedTemporaryFile(
            delete=False,
            suffix=".pdf"
        ) as temp_file:

            temp_file.write(
                uploaded_file.getbuffer()
            )

            temp_path = temp_file.name

        try:

            num_chunks = ingest_pdf(
                temp_path,
                document_name=uploaded_file.name
            )

            st.sidebar.success(
                f"Processed {uploaded_file.name} "
                f"({num_chunks} chunks)"
            )

        except Exception as e:

            st.sidebar.error(
                f"Error: {e}"
            )

        finally:

            if os.path.exists(temp_path):
                os.remove(temp_path)


# ==========================================================
# AVAILABLE PAPERS
# ==========================================================

collection = create_chroma_collection()

data = collection.get()

available_papers = sorted({
    metadata["document_name"]
    for metadata in data["metadatas"]
})


# ==========================================================
# PAPER SELECTION
# ==========================================================

if available_papers:

    selected_paper = st.selectbox(
        "Select papers",
        ["All papers"] + available_papers
    )

else:

    selected_paper = "All papers"

    st.info(
        "Upload and process at least one research paper."
    )


# ==========================================================
# QUESTION
# ==========================================================

query = st.text_input(
    "Ask a question about your research papers:"
)


# ==========================================================
# ASK QUESTION
# ==========================================================

if st.button("Ask") and query:

    with st.spinner(
        "Searching research papers..."
    ):

        if selected_paper == "All papers":

            retrieved_chunks = retrieve_hybrid(
                query,
                top_k_vector=10,
                top_k_bm25=10
            )

        else:

            retrieved_chunks = retrieve_hybrid(
                query,
                top_k_vector=10,
                top_k_bm25=10,
                document_name=selected_paper
            )


    with st.spinner(
        "Generating answer..."
    ):

        answer = generate_answer(
            query,
            retrieved_chunks
        )


    # ======================================================
    # ANSWER
    # ======================================================

    st.subheader("Answer")

    st.write(answer)


    # ======================================================
    # SOURCES
    # ======================================================

    st.subheader("Sources")

    for i, chunk in enumerate(
        retrieved_chunks,
        start=1
    ):

        with st.expander(
            f"Source {i}"
        ):

            st.write(
                f"**Paper:** "
                f"{chunk['document_name']}"
            )

            st.write(
                f"**Page:** "
                f"{chunk['page_number']}"
            )

            st.write(
                chunk["text"]
            )