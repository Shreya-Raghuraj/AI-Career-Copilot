from groq import Groq
import os
import json
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))


def generate_resume_score(resume_text, job_matches):

    if not job_matches:
        return {}

    best_match = job_matches[0]

    matched = len(best_match["matched_skills"])
    missing = len(best_match["missing_skills"])

    total = matched + missing

    if total == 0:
        ats_score = 0
    else:
        ats_score = int((matched / total) * 100)

    skills_score = min(matched * 4, 20)

    projects_score = 16

    formatting_score = 18

    experience_score = 12

    overall_score = int(
        ats_score * 0.4 +
        skills_score * 5 * 0.2 +
        projects_score * 5 * 0.15 +
        formatting_score * 5 * 0.15 +
        experience_score * 5 * 0.1
    )

    return {
        "overall_score": overall_score,
        "ats_score": ats_score,
        "skills_score": skills_score,
        "projects_score": projects_score,
        "formatting_score": formatting_score,
        "experience_score": experience_score,
    }