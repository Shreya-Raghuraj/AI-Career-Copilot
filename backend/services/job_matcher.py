import pandas as pd


def match_jobs(user_skills):
    jobs = pd.read_csv("data/job_roles.csv")

    results = []

    user_skills = set(skill.lower() for skill in user_skills)

    for _, row in jobs.iterrows():

        required = [s.strip() for s in row["required_skills"].split(",")]

        required_lower = set(skill.lower() for skill in required)

        matched = sorted(
            skill for skill in required
            if skill.lower() in user_skills
        )

        missing = sorted(
            skill for skill in required
            if skill.lower() not in user_skills
        )

        score = round((len(matched) / len(required)) * 100)

        results.append({
            "role": row["role"],
            "match_score": score,
            "matched_skills": matched,
            "missing_skills": missing
        })

    results.sort(key=lambda x: x["match_score"], reverse=True)

    return results