from document_loader import load_document
from chunker import create_chunks
from emeddings import create_embeddings
from vector_store import create_faiss_index
from retriever import search
from sentence_transformers import SentenceTransformer
from llm import generate_answer


documents = load_document("../documents")
chunks = create_chunks(documents, chunk_size=800, overlap=100)
embeddings = create_embeddings(chunks)
index = create_faiss_index(embeddings)
model = SentenceTransformer('all-MiniLM-L6-v2')
query = input("Enter your query: ")
results = search(index, model, query, chunks, top_k=5)
context = ""

for result in results:
    context += f"""
Source: {result["source"]}
Page: {result["page"]}

{result["text"]}

"""
print("\n" + "=" * 60)
print("RETRIEVED CONTEXT")
print("=" * 60)

print("\n" + "=" * 60)
print("SOURCES")
print("=" * 60)

unique_sources = set()

for result in results:
    source = result["source"]
    page = result["page"]

    source_info = (source, page)

    if source_info not in unique_sources:
        print(f"- {source} | Page {page}")
        unique_sources.add(source_info)

answer = generate_answer(query, context)
print("\nAnswer:")
print(answer)