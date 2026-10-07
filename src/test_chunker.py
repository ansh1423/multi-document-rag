from document_loader import load_document
from chunker import create_chunks

documents = load_document("../documents")
chunks = create_chunks(documents, chunk_size=500, overlap=50)

for i in range(min(5, len(chunks))):
    print("Chunk", i + 1)
    print("Source:", chunks[i]["source"])
    print("Page:", chunks[i]["page"])
    print("Text:", chunks[i]["text"][:100])
    print("-" * 50)