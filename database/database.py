import sqlite3

conn = sqlite3.connect("database/resumes.db", check_same_thread=False)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS candidates(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    candidate_name TEXT,
    match_score REAL,
    prediction TEXT,
    matched_skills TEXT,
    missing_skills TEXT
)
""")

conn.commit()


def save_candidate(name, score, prediction, matched, missing):

    cursor.execute("""
    INSERT INTO candidates(
        candidate_name,
        match_score,
        prediction,
        matched_skills,
        missing_skills
    )
    VALUES (?,?,?,?,?)
    """, (
        name,
        score,
        prediction,
        ", ".join(matched),
        ", ".join(missing)
    ))

    conn.commit()


def get_all_candidates():

    cursor.execute("SELECT * FROM candidates")

    return cursor.fetchall()