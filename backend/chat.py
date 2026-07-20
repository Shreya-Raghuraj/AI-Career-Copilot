from fastapi import APIRouter
from pydantic import BaseModel
from groq import Groq
from dotenv import load_dotenv
import os
import time
from typing import Any

load_dotenv()

router = APIRouter()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))


class ChatRequest(BaseModel):
    message: str
    resume_data: dict[str, Any] | None = None
    chat_history: list[dict[str, Any]] = []


@router.post("/chat")
def chat(request: ChatRequest):

    resume = request.resume_data or {}

    skills = resume.get("skills", [])
    job_matches = resume.get("job_matches", [])
    resume_score = resume.get("resume_score", {})
    roadmap = resume.get("roadmap", [])

    prompt = f"""
You are an AI Career Coach.

You have already analyzed the student's resume.

Do NOT introduce yourself in every response.
Do NOT repeat that you have their resume unless they ask.

Give concise, practical advice based on the resume analysis.

Resume Skills:
{skills}

Recommended Jobs:
{job_matches}

Resume Score:
{resume_score}

Learning Roadmap:
{roadmap}

Current User Question:
{request.message}
"""

    start = time.time()

    history = []

    for msg in request.chat_history:
        history.append(
            {
                "role": "assistant" if msg["sender"] == "ai" else "user",
                "content": msg["text"],
            }
        )

    messages = history + [
        {
            "role": "user",
            "content": prompt,
        }
    ]

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=messages,
    )

    end = time.time()
    print(f"AI Response Time: {end - start:.2f} seconds")

    return {
        "reply": response.choices[0].message.content
    }