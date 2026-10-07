from document_loader import load_document
from chunker import create_chunks
from emeddings import create_embeddings

documents = load_document("../documents")
chunks = create_chunks(documents, chunk_size=500, overlap=50)
embeddings = create_embeddings(chunks)

print("\nTotal chunks:", len(chunks))
print("Embeddings shape:", embeddings.shape)

print("\nFirst embedding:")
print(embeddings[0])