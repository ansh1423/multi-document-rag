from document_loader import load_document
from chunker import create_chunks


documents = load_document("../documents")

chunks = create_chunks(
    documents,
    chunk_size=800,
    overlap=100
)

for i, chunk in enumerate(chunks):
    if chunk["source"] == "1 sem m.a.pdf":
        print("\n" + "=" * 70)
        print("Chunk:", i)
        print("Source:", chunk["source"])
        print("Page:", chunk["page"])
        print("=" * 70)
        print(chunk["text"])