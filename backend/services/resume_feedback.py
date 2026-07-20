import os
from dotenv import load_dotenv
from groq import Groq
from backend.rag.retriever import retrieve_documents

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))


def get_resume_feedback(resume_text: str, job_role: str):

    docs = retrieve_documents(job_role)

    context = "\n\n".join(
        [doc.page_content for doc in docs]
    )

    prompt = f"""
You are an expert resume reviewer.

Job Role:
{job_role}

Relevant Career Knowledge:
{context}

Resume:
{resume_text}

Provide:

1. Resume strengths
2. Resume weaknesses
3. Missing skills
4. Improvement suggestions
5. Final recommendation

Keep the response professional.
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