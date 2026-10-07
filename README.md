# Multi-Document RAG Knowledge Assistant

A practical **Retrieval-Augmented Generation (RAG)** system that allows users to ask questions across multiple PDF documents and receive grounded answers using semantic search and an LLM.

The project is built from scratch using **Python, Sentence Transformers, FAISS, and OpenRouter**, without relying on LangChain, to understand the core components of a RAG pipeline.

---

## 🚀 Features

- 📄 Load multiple PDF documents
- 📑 Extract text page by page
- ✂️ Split documents into overlapping chunks
- 🧠 Generate semantic embeddings using Sentence Transformers
- 🔎 Perform semantic similarity search using FAISS
- 🎯 Metadata-aware retrieval using document names
- 🤖 Generate answers using an LLM through OpenRouter
- 📚 Answer questions using information from multiple documents
- 🛡️ Reduce hallucination by restricting answers to retrieved context
- 📌 Display source document and page number for retrieved information

---

## 🏗️ RAG Architecture

```text
                 PDF Documents
                       │
                       ▼
              Document Loader
                       │
                       ▼
              Text Chunking
              (800 chars)
                       │
                       ▼
           Sentence Transformers
              Embeddings
                       │
                       ▼
                  FAISS
              Vector Search
                       │
                       ▼
                User Query
                       │
                       ▼
           Metadata-Aware Retrieval
                       │
                       ▼
             Relevant Chunks
                       │
                       ▼
               Context Builder
                       │
                       ▼
              OpenRouter LLM
                       │
                       ▼
               Grounded Answer
                       │
                       ▼
              Source + Page
```

---

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| PyPDF | PDF text extraction |
| Sentence Transformers | Text embeddings |
| `all-MiniLM-L6-v2` | Embedding model |
| FAISS | Vector similarity search |
| OpenRouter | LLM API |
| Requests | API communication |
| python-dotenv | Environment variable management |

---

## 📂 Project Structure

```text
Multi-Document RAG/
│
├── documents/
│   └── .gitkeep
│
├── src/
│   ├── chunker.py
│   ├── document_loader.py
│   ├── emeddings.py
│   ├── llm.py
│   ├── main.py
│   ├── retriever.py
│   ├── vector_store.py
│   │
│   ├── test_chunker.py
│   ├── test_document_chunks.py
│   ├── test_embedder.py
│   ├── test_llm.py
│   ├── test_loader.py
│   ├── test_rag.py
│   ├── test_retriever.py
│   └── test_vector_store.py
│
├── .gitignore
└── README.md
```

> Personal PDF documents are intentionally not included in the repository.

---

## ⚙️ How the RAG Pipeline Works

### 1. Document Loading

PDF files are loaded using PyPDF.

Each page is stored along with metadata:

```python
{
    "text": "...",
    "source": "document.pdf",
    "page": 1
}
```

This allows the system to identify where retrieved information came from.

---

### 2. Chunking

Large PDF pages are divided into smaller chunks.

Current configuration:

```python
chunk_size = 800
overlap = 100
```

This means each chunk contains approximately 800 characters, while 100 characters overlap with the next chunk.

The overlap helps preserve context when important information appears near a chunk boundary.

---

### 3. Embeddings

Each chunk is converted into a numerical vector using:

```text
sentence-transformers/all-MiniLM-L6-v2
```

These embeddings allow the system to compare the semantic similarity between a user's question and document chunks.

---

### 4. FAISS Vector Search

The generated embeddings are stored in a FAISS index.

When a user asks a question:

```text
User Query
    ↓
Query Embedding
    ↓
FAISS Similarity Search
    ↓
Most Relevant Chunks
```

---

### 5. Metadata-Aware Retrieval

The system can detect when the user specifies a particular PDF.

For example:

```text
What is the CGPA mentioned in the 1 sem m.a.pdf document?
```

The retriever identifies:

```text
1 sem m.a.pdf
```

and restricts the retrieved results to that document.

This prevents unrelated documents from influencing the answer.

---

### 6. Top-K Retrieval

The current retrieval configuration uses:

```python
top_k = 5
```

This means the system retrieves the **5 most relevant chunks** for the query.

A larger `top_k` provides more context but may introduce irrelevant information.

A smaller `top_k` provides more focused context but may miss useful information.

---

### 7. LLM Generation

The retrieved chunks are passed to an LLM through OpenRouter.

The LLM is instructed to answer using only the provided context.

If the required information is unavailable, the system responds:

```text
I don't have enough information in the provided documents.
```

This helps reduce hallucinations.

---

## 🧪 Example Queries

### Single-document question

```text
What is the CGPA mentioned in the 1 sem m.a.pdf document?
```

Example answer:

```text
The CGPA mentioned in the 1 sem m.a.pdf document is 8.416.
```

Source:

```text
1 sem m.a.pdf | Page 1
```

---

### Multi-document question

```text
What CGPA values are mentioned in the semester documents?
```

Example answer:

```text
1st semester: 8.416
3rd semester: 8.111
```

---

### Unsupported question

```text
What is Ansh's favorite programming language?
```

Expected behavior:

```text
I don't have enough information in the provided documents.
```

The system does not invent an answer when the information is unavailable.

---

## 🔐 Environment Variables

Create a `.env` file in the project root:

```env
OPENROUTER_API_KEY=your_api_key_here
```

Never commit your real API key to GitHub.

The `.gitignore` file excludes:

```text
.env
venv/
documents/*.pdf
__pycache__/
```

---

## 📦 Installation

Clone the repository:

```bash
git clone https://github.com/ansh1423/multi-document-rag.git
```

Move into the project:

```bash
cd multi-document-rag
```

Create a virtual environment:

```bash
python3 -m venv venv
```

Activate it on macOS/Linux:

```bash
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r src/requirements.txt
```

Add your PDF files to:

```text
documents/
```

Create your `.env` file and add your OpenRouter API key.

---

## ▶️ Running the Project

From the `src` directory:

```bash
cd src
```

Run the complete RAG pipeline:

```bash
python3 test_rag.py
```

Enter a question when prompted.

Example:

```text
Enter your query: What is the CGPA mentioned in the 1 sem m.a.pdf document?
```

---

## 🧠 Key RAG Concepts Demonstrated

This project demonstrates the core components of a RAG system:

- Document ingestion
- PDF parsing
- Chunking
- Chunk overlap
- Embeddings
- Vector databases
- Semantic search
- Top-K retrieval
- Metadata filtering
- Context construction
- LLM generation
- Grounded responses
- Hallucination prevention
- Source tracking

---

## 🎯 Learning Objectives

The main goal of this project was to understand **how RAG works internally** instead of depending completely on high-level frameworks.

The project was intentionally implemented without LangChain so that each major RAG component could be understood and tested independently.

---

## 🔮 Future Improvements

Possible future improvements include:

- Reranking retrieved chunks
- Hybrid search (keyword + semantic search)
- Better chunking strategies
- Persistent FAISS indexes
- Streaming LLM responses
- Conversation memory
- Web-based UI
- Authentication
- Document upload interface
- Better source citation formatting
- Evaluation of retrieval accuracy
- LangChain/LangGraph implementation

---

## 👨‍💻 Author

**Ansh Yadav**

Interested in:

- AI Engineering
- Generative AI
- Agentic AI
- RAG Systems
- Python Automation
- AI-powered Applications

GitHub: `https://github.com/ansh1423`

---

## ⭐ Project Status

**Completed ✅**

This project successfully implements and tests a complete multi-document RAG pipeline with semantic retrieval, metadata-aware search, grounded LLM generation, and source tracking.
