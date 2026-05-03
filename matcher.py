import re

# Simple skill list (you can expand)
SKILLS_DB = [
    "python", "java", "sql", "machine learning", "deep learning",
    "nlp", "flask", "streamlit", "django", "pandas",
    "numpy", "aws", "docker", "git", "linux"
]

def extract_skills(text):
    text = text.lower()
    found_skills = []

    for skill in SKILLS_DB:
        if re.search(r"\b" + re.escape(skill) + r"\b", text):
            found_skills.append(skill)

    return set(found_skills)


def calculate_match_score(resume_skills, job_skills):
    if not job_skills:
        return 0

    matched = resume_skills.intersection(job_skills)

    score = (len(matched) / len(job_skills)) * 100
    return round(score, 2)