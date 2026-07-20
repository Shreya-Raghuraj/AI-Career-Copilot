import pandas as pd

def generate_roadmap(missing_skills):
    resources = pd.read_csv("data/learning_resources.csv")

    roadmap = []

    for skill in missing_skills:
        matches = resources[
            resources["skill"].str.lower() == skill.lower()
        ]

        if not matches.empty:
            roadmap.append({
                "skill": skill,
                "resources": matches.to_dict(orient="records")
            })

    return roadmap