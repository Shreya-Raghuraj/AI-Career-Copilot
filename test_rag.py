from backend.rag.retriever import retrieve_documents

docs = retrieve_documents(
    "Frontend Developer React HTML CSS"
)

for i, doc in enumerate(docs):

    print("=" * 60)
    print(f"Document {i+1}")
    print(doc.metadata)
    print(doc.page_content[:500])