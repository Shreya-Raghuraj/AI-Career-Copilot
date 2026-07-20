import os

from dotenv import load_dotenv
from groq import Groq

from backend.rag.retriever import retrieve_documents

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))


def career_chat(query: str):

    docs = retrieve_documents(query)

    context = "\n\n".join(
        [doc.page_content for doc in docs]
    )

    prompt = f"""
You are an expert AI Career Coach.

Answer ONLY using the retrieved career knowledge below.

=========================
CAREER KNOWLEDGE
=========================

{context}

=========================
USER QUESTION
=========================

{query}

Provide a clear, structured answer.

If the retrieved documents do not contain enough information, say so instead of making up facts.
"""

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
        {
            "role": "user",
            "content": prompt
        }
    ]
)
    return response.choices[0].message.content