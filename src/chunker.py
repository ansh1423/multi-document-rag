def create_chunks(documents, chunk_size=800, overlap=100):
    chunks = []

    for document in documents:
        text = document["text"]
        start = 0

        while start < len(text):
            end = start + chunk_size
            chunk_text = text[start:end]

            chunks.append({
                "text": chunk_text,
                "source": document["source"],
                "page": document["page"]
            })

            start = end - overlap

    return chunks