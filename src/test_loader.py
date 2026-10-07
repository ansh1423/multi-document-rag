from document_loader import load_document

documents = load_document("../documents")
print("Total page loaded:", len(documents))

for document in documents:
    print("Source:", document["source"])
    print("Page:", document["page"])
    print("Text:", document["text"][:100])
    print("-" * 50)