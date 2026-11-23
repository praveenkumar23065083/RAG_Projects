# 📚 PaperLens – Research Paper RAG Assistant

**An intelligent, RAG-powered research assistant that enables users to interact with multiple research papers, retrieve relevant information, and generate context-aware answers with source citations.**

PaperLens is an end-to-end Retrieval-Augmented Generation (RAG) application designed to make research paper exploration faster and more efficient. Instead of manually searching through lengthy academic PDFs, users can upload research papers, ask natural language questions, and receive answers grounded in the retrieved document content.

The system combines dense vector retrieval, sparse keyword-based retrieval, and reranking to improve the relevance and reliability of retrieved information.

---

## 🚀 Key Features

- **Multi-PDF Support:** Upload and process multiple research papers simultaneously.
- **PDF Ingestion:** Extract text and document information using PyMuPDF.
- **Intelligent Chunking:** Split documents into manageable chunks with overlapping context to preserve semantic continuity.
- **Dense Vector Retrieval:** Generate semantic embeddings using BAAI's BGE-small embedding model.
- **Sparse Retrieval:** Use BM25 to retrieve relevant passages based on keyword matching.
- **Hybrid Search:** Combine dense and sparse retrieval to capture both semantic similarity and exact keyword matches.
- **Reranking:** Improve retrieval quality by reranking candidate passages based on their relevance to the query.
- **Context-Grounded Answers:** Generate responses using retrieved document passages rather than relying solely on the LLM's internal knowledge.
- **Source Citations:** Provide supporting document and page references to help users verify generated answers.
- **Insufficient Evidence Handling:** Avoid generating unsupported answers when the retrieved context does not contain sufficient information.

---

## 🏗️ System Architecture

PaperLens follows a modular RAG architecture consisting of two major pipelines:

### 1. Document Ingestion Pipeline

The ingestion pipeline converts uploaded research papers into searchable document representations.

1. **PDF Upload:** Users upload one or more research papers.
2. **Text Extraction:** PyMuPDF extracts textual content from the PDFs.
3. **Text Chunking:** Extracted content is divided into overlapping chunks (approximately 500–800 tokens with 100-token overlap).
4. **Embedding Generation:** BGE-small generates 384-dimensional vector embeddings for each chunk.
5. **Vector Storage:** Embeddings and associated metadata are stored in ChromaDB.
6. **Keyword Indexing:** BM25 builds a sparse retrieval index for keyword-based search.

### 2. Query & Retrieval Pipeline

When a user asks a question, PaperLens retrieves relevant information through a hybrid retrieval process.

1. **Query Input:** The user submits a natural language question.
2. **Dense Retrieval:** The query is embedded and searched against ChromaDB.
3. **Sparse Retrieval:** BM25 retrieves documents based on keyword relevance.
4. **Hybrid Retrieval:** Results from both retrieval methods are combined.
5. **Reranking:** A reranker evaluates and improves the ordering of retrieved candidates.
6. **Context Construction:** The most relevant passages and their metadata are assembled into the LLM context.
7. **Answer Generation:** The LLM generates a response grounded in the retrieved context.
8. **Source Attribution:** Relevant document and page references are provided alongside the answer.

**Workflow Diagram**

<img width="1450" height="1232" alt="image" src="https://github.com/user-attachments/assets/ca5a2a0b-d5fc-4621-9bbd-4daba4019360" />


---

## 🧰 Tech Stack

| Component | Technology |
|---|---|
| Programming Language | Python |
| Frontend | Streamlit |
| PDF Processing | PyMuPDF |
| Embedding Model | BAAI/bge-small-en-v1.5 |
| Vector Database | ChromaDB |
| Sparse Retrieval | BM25 |
| Retrieval Strategy | Hybrid Search |
| Reranking | Reranker |
| LLM | GPT-OSS 120B |
| LLM API | Groq API |

---

## 📂 Project Structure

```text
PaperLens/
│
├── chroma_db/                 # Persistent vector database
│
├── app.py                     # Main Streamlit application
│
├── test_chroma.py             # ChromaDB functionality tests
├── test_chroma_count.py       # Vector database count checks
├── test_chunking.py           # Text chunking tests
├── test_embeddings.py         # Embedding generation tests
├── test_hybrid.py             # Hybrid retrieval tests
├── test_ingestion.py          # Document ingestion tests
├── test_reranker.py           # Reranking tests
├── test_retrieval.py          # Retrieval pipeline tests
│
└── README.md                  # Project documentation
```

---

## ⚙️ Core Technical Concepts

### 1. Dense Retrieval
Uses semantic embeddings to retrieve passages based on the contextual similarity between the user's query and document chunks.

**Embedding Model:** `BAAI/bge-small-en-v1.5`

### 2. Sparse Retrieval – BM25
Uses keyword-based ranking to identify relevant passages, making it particularly useful for exact terminology, technical terms, and specific research concepts.

### 3. Hybrid Retrieval
Combines dense semantic search and sparse keyword retrieval to improve the coverage and relevance of retrieved information.

### 4. Reranking
The retrieved candidates are passed through a reranking stage to prioritize the passages most relevant to the user's query before context construction.

### 5. Grounded Generation
The LLM generates answers using retrieved document context, with source references to support verification and reduce unsupported responses.

---

## 🎯 Objectives & Learning Outcomes

Building PaperLens provided hands-on experience with:

- Designing an end-to-end Retrieval-Augmented Generation pipeline.
- Understanding document ingestion, chunking, and embedding generation.
- Implementing dense, sparse, and hybrid retrieval strategies.
- Working with vector databases and persistent embeddings.
- Improving retrieval quality through reranking.
- Integrating open-source LLMs through OpenRouter.
- Managing document metadata and source-level citations.
- Building a user-facing application using Streamlit.
- Implementing insufficient-evidence handling for more reliable responses.

---

## 🔮 Future Improvements

- Advanced retrieval strategies and query expansion.
- RAG evaluation using metrics such as Recall@K, MRR, and faithfulness.
- Conversation memory for multi-turn research discussions.
- Improved document parsing for tables, figures, and mathematical equations.
- Deployment and performance optimization.

---

## 👨‍💻 Author

**Praveen Kumar**

Final-year Civil Engineering Student | IIT (BHU), Varanasi

Interested in Machine Learning, Deep Learning, NLP, LLMs, and Generative AI.


---

*PaperLens demonstrates the practical application of Retrieval-Augmented Generation for academic research and document intelligence.*
