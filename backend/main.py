from fastapi import FastAPI, UploadFile, File
from .chat import router as chat_router
from fastapi.middleware.cors import CORSMiddleware
import os
import shutil

from backend.services.resume_parser import extract_text_from_pdf
from backend.services.skill_extractor import extract_skills
from backend.services.job_matcher import match_jobs
from backend.services.roadmap_generator import generate_roadmap
from backend.services.resume_feedback import get_resume_feedback
from backend.services.resume_score import generate_resume_score
from backend.services.chatbot import career_chat

print("Backend started")

app = FastAPI(title="AI Career Co-Pilot")
app.include_router(chat_router)
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@app.get("/")
def home():
    return {"message": "Backend is running!"}


@app.post("/upload-resume")
async def upload_resume(file: UploadFile = File(...)):

    file_path = os.path.join(UPLOAD_FOLDER, file.filename)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # Resume Parsing
    text = extract_text_from_pdf(file_path)

    # Skill Extraction
    skills = extract_skills(text)

    # Job Matching
    job_matches = match_jobs(skills)

    # Learning Roadmap
    roadmap = []

    if job_matches:
        best_match = job_matches[0]
        roadmap = generate_roadmap(best_match["missing_skills"])

    # AI Resume Feedback
    ai_feedback = get_resume_feedback(
    text,
    best_match["role"]
)

    resume_score = generate_resume_score(text, job_matches)

    return {
        "filename": file.filename,
        "skills": skills,
        "job_matches": job_matches,
        "roadmap": roadmap,
        "ai_feedback": ai_feedback,
        "resume_score": resume_score,
    }
from pydantic import BaseModel

class ChatRequest(BaseModel):
    query: str


@app.post("/career-chat")
def chat(request: ChatRequest):

    answer = career_chat(request.query)

    return {
        "query": request.query,
        "answer": answer
    }