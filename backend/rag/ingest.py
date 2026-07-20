import os

from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter

from backend.rag.vector_store import get_vector_store

DOCUMENTS_PATH = "documents"


def load_documents():
    documents = []

    for root, _, files in os.walk(DOCUMENTS_PATH):
        for file in files:
            if file.endswith(".txt"):

                file_path = os.path.join(root, file)

                with open(file_path, "r", encoding="utf-8") as f:
                    text = f.read()

                if text.strip():

                    documents.append(
                        Document(
                            page_content=text,
                            metadata={"source": file_path}
                        )
                    )

    return documents


def ingest_documents():

    print("📂 Loading documents...")

    documents = load_documents()

    print(f"✅ Loaded {len(documents)} documents")

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=800,
        chunk_overlap=100
    )

    chunks = splitter.split_documents(documents)

    print(f"✅ Created {len(chunks)} chunks")

    vector_store = get_vector_store()

    vector_store.add_documents(chunks)

    print("🎉 Documents added to ChromaDB!")


if __name__ == "__main__":
    ingest_documents()