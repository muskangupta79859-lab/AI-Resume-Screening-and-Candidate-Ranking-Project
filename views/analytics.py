import streamlit as st
import pandas as pd
import plotly.express as px
from utils.matching import calculate_match


def show_analytics():

    st.header("📊 Analytics Dashboard")

    if "jd_skills" not in st.session_state:

        st.warning("Please analyze a Job Description first.")
        return

    if "resumes" not in st.session_state:

        st.warning("Please upload resumes first.")
        return

    results = []

    jd_skills = st.session_state["jd_skills"]

    for resume in st.session_state["resumes"]:

        matched, missing, score = calculate_match(
            resume["skills"],
            jd_skills
        )

        results.append({
            "Candidate": resume["name"],
            "Match": score
        })

    df = pd.DataFrame(results)

    st.subheader("Candidate Match Percentage")

    fig = px.bar(
        df,
        x="Candidate",
        y="Match",
        text="Match",
        title="Candidate Ranking"
    )

    st.plotly_chart(fig, use_container_width=True)