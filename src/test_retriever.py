from document_loader import load_document
from chunker import create_chunks
from emeddings import create_embeddings
from vector_store import create_faiss_index
from retriever import search
from sentence_transformers import SentenceTransformer

documents = load_document("../documents")
chunks = create_chunks(documents, chunk_size=500, overlap=50)
embeddings = create_embeddings(chunks)
index = create_faiss_index(embeddings)
model = SentenceTransformer('all-MiniLM-L6-v2')

query = "What AI technologies does Ansh know?"
results = search(index, model, query, chunks, top_k=5)

print("\nTop 3 results for the query:", query)
for i, result in enumerate(results):
    print("\n"+"-"*60)
    print("Result : ",i)
    print("Source:", result["source"])
    print("Page:", result["page"])
    # print("Text:", result["text"][:200])
    print(result["text"])
    