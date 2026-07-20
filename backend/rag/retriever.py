from backend.rag.vector_store import get_vector_store


def retrieve_documents(query: str, k: int = 3):

    vector_store = get_vector_store()

    docs = vector_store.similarity_search(
        query,
        k=k
    )

    return docs