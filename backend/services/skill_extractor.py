import pandas as pd
import re


def extract_skills(resume_text):
    skills_df = pd.read_csv("data/skills.csv")

    extracted_skills = []

    resume_text = resume_text.lower()

    for skill in skills_df["skill"]:
        pattern = r"\b" + re.escape(skill.lower()) + r"\b"

        if re.search(pattern, resume_text):
            extracted_skills.append(skill)

    return sorted(set(extracted_skills))