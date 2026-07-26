import joblib

model = joblib.load("models/candidate_model.pkl")

def predict_candidate(match_score, matched_skills, missing_skills):

    prediction = model.predict([[
        match_score,
        matched_skills,
        missing_skills
    ]])

    return prediction[0]