from document_loader import load_document
from chunker import create_chunks
from emeddings import create_embeddings
from vector_store import create_faiss_index

documents = load_document("../documents")
chunks = create_chunks(documents, chunk_size=500, overlap=50)
embeddings = create_embeddings(chunks)
index = create_faiss_index(embeddings)

print("\nTotal chunks:", len(chunks))
print("Embedding shape:", embeddings.shape)
print("FAISS index size:", index.ntotal)
print("FAISS dimension:", index.d)