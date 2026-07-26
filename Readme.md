# 🤖 AI Resume Screening & Candidate Ranking System
![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-App-red?logo=streamlit)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-ML-orange?logo=scikitlearn)
![License](https://img.shields.io/badge/License-MIT-green)

An AI-powered Resume Screening System that automatically analyzes resumes, extracts candidate skills using NLP, compares them with a Job Description, ranks candidates based on skill matching, predicts candidate suitability using Machine Learning, and generates interview questions.

---

## 🚀 Live Demo

🔗https://ai-resume-screening-and-candidate-ranking-project-nn9wpmaj8fic.streamlit.app/

---

## 📌 Features

- 📄 Upload multiple resumes (PDF/DOCX)
- 📝 Upload or paste Job Description
- 🧹 Resume & Job Description preprocessing
- 🧠 NLP-based Skill Extraction
- 🎯 Skill Matching with Job Description
- 📊 Candidate Match Score Calculation
- 🤖 Machine Learning Candidate Prediction
- 🏆 Candidate Ranking
- 💬 AI-generated Interview Questions
- 📄 Download Candidate Report (PDF)
- 📤 Export Candidate Ranking to CSV
- 🔍 Search & Filter Candidates
- 📈 Analytics Dashboard
- 💾 SQLite Database Integration
- 🎨 Modern Streamlit UI
- 🔎 Resume Search & Candidate Filtering

---

## 🛠️ Tech Stack

### Programming Language
- Python

### Machine Learning
- Scikit-learn
- Joblib

### Natural Language Processing
- NLTK
- spaCy

### Data Processing
- Pandas
- NumPy

### Visualization
- Plotly
- Matplotlib

### Frontend
- Streamlit
- Streamlit Option Menu
- Custom CSS

### Database
- SQLite

### Report Generation
- ReportLab
- PyPDF2
- pdfplumber

---

## 📂 Project Structure

```text
AI-Resume-Screening-and-Candidate-Ranking-System/

│── app.py
│── README.md
│── requirements.txt
│── train_model.py

├── assets/
│      style.css

├── data/
│      skills.csv

├── database/
│      database.py

├── models/
│      candidate_model.pkl

├── views/
│      home.py
│      upload_resume.py
│      job_description.py
│      candidate_ranking.py
│      analytics.py

├── utils/
│      parser.py
│      preprocessing.py
│      skill_extractor.py
│      matching.py
│      predictor.py
│      pdf_generator.py
│      interview_generator.py
```

---

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/muskangupta79859-lab/AI-Resume-Screening-and-Candidate-Ranking-System.git
```

### Move into Project

```bash
cd AI-Resume-Screening-and-Candidate-Ranking-System
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run the Application

```bash
streamlit run app.py
```

---


## 📊 Workflow

```text
Upload Resume
        │
        ▼
Resume Parsing
        │
        ▼
Text Preprocessing
        │
        ▼
Skill Extraction
        │
        ▼
Upload Job Description
        │
        ▼
Skill Matching
        │
        ▼
Match Score Calculation
        │
        ▼
ML Prediction
        │
        ▼
Candidate Ranking
        │
        ▼
Analytics + PDF + CSV
```

---

## 🎯 Machine Learning Model

The project uses a Machine Learning model trained to classify candidates into different suitability levels based on:

- Match Score
- Number of Matched Skills
- Number of Missing Skills

Prediction Categories:

- 🟢 Highly Suitable
- 🔵 Suitable
- 🟡 Moderately Suitable
- 🔴 Not Suitable

---

## 🔮 Future Enhancements

- Resume Similarity Score
- Email Candidate Reports
- Recruiter Login System
- Cloud Database Integration
- LLM-powered Resume Feedback
- AI Resume Improvement Suggestions

---

## 👩‍💻 Developed By

**Muskan Gupta**

B.Tech CSE (Artificial Intelligence)

---

## ⭐ If you found this project useful

Please consider giving it a ⭐ on GitHub.