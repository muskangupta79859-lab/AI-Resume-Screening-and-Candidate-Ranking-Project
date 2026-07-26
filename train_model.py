import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib

# Dummy training dataset
data = pd.DataFrame({
    "match_score": [95,90,85,80,75,70,65,60,55,50,45,40,35,30],
    "matched_skills": [10,9,8,8,7,7,6,5,5,4,4,3,2,1],
    "missing_skills": [0,1,2,2,3,3,4,5,5,6,6,7,8,9],
    "label": [
        "Highly Suitable",
        "Highly Suitable",
        "Highly Suitable",
        "Suitable",
        "Suitable",
        "Suitable",
        "Suitable",
        "Moderately Suitable",
        "Moderately Suitable",
        "Moderately Suitable",
        "Not Suitable",
        "Not Suitable",
        "Not Suitable",
        "Not Suitable"
    ]
})

X = data[["match_score","matched_skills","missing_skills"]]
y = data["label"]

model = RandomForestClassifier(random_state=42)
model.fit(X, y)

joblib.dump(model, "models/candidate_model.pkl")

print("✅ Model Saved Successfully")