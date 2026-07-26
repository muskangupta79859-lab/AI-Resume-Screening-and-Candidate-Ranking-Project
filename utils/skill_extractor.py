import pandas as pd

# Load skills from CSV
skills_df = pd.read_csv("data/skills.csv")
SKILLS = skills_df["Skill"].str.lower().tolist()


def extract_skills(text):
    """
    Extract matching skills from resume text.
    """
    text = text.lower()

    found_skills = []

    for skill in SKILLS:
        if skill in text:
            found_skills.append(skill.title())

    return sorted(list(set(found_skills)))