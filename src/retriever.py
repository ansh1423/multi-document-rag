import re
import numpy as np
import faiss


def normalize_text(text):
    return re.sub(r"\s+", " ", text.lower().strip())


def find_requested_source(query, chunks):
    """
    Check whether the user mentioned one of the PDF filenames
    in the query.
    """

    normalized_query = normalize_text(query)

    sources = sorted(
        {chunk["source"] for chunk in chunks},
        key=len,
        reverse=True
    )

    for source in sources:
        if normalize_text(source) in normalized_query:
            return source

    return None


def search(index, model, query, chunks, top_k=5):
    """
    Perform semantic search.

    If the user mentions a specific PDF source,
    search only inside that document.
    """

    query_embedding = model.encode([query])

    query_embedding = np.array(
        query_embedding
    ).astype("float32")

    requested_source = find_requested_source(
        query,
        chunks
    )

    # ------------------------------------------------
    # CASE 1: User specified a particular PDF
    # ------------------------------------------------

    if requested_source:

        candidate_indices = [
            i
            for i, chunk in enumerate(chunks)
            if chunk["source"] == requested_source
        ]

        # Search the complete FAISS index first.
        distances, indices = index.search(
            query_embedding,
            index.ntotal
        )

        filtered_results = []

        for distance, index_position in zip(
            distances[0],
            indices[0]
        ):
            if index_position in candidate_indices:
                filtered_results.append(
                    (distance, index_position)
                )

                if len(filtered_results) == top_k:
                    break

        selected_results = filtered_results

    # ------------------------------------------------
    # CASE 2: No specific PDF mentioned
    # ------------------------------------------------

    else:

        k = min(top_k, index.ntotal)

        distances, indices = index.search(
            query_embedding,
            k
        )

        selected_results = list(
            zip(
                distances[0],
                indices[0]
            )
        )

    # ------------------------------------------------
    # Convert results into dictionaries
    # ------------------------------------------------

    results = []

    for distance, index_position in selected_results:

        results.append({
            "text": chunks[index_position]["text"],
            "source": chunks[index_position]["source"],
            "page": chunks[index_position]["page"],
            "distance": float(distance)
        })

    return results