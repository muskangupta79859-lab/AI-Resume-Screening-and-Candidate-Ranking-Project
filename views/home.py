import streamlit as st
from views.upload_resume import show_upload_resume
from views.job_description import show_job_description

def show_home():

    st.markdown("""
    # 🤖 AI Resume Screening System

    ### Intelligent Candidate Ranking using Machine Learning, NLP & Deep Learning

    Automatically analyze resumes, compare them with job descriptions, rank candidates and generate interview questions.
    """)

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("📄 Resumes", "0")
    col2.metric("🎯 Match Score", "0%")
    col3.metric("🏆 Ranked", "0")
    col4.metric("🤖 AI Models", "3")

    st.subheader("✨ Features")

    c1, c2 = st.columns(2)

    with c1:
        st.success("📄 Upload multiple resumes")
        st.success("🧠 NLP Skill Extraction")
        st.success("🤖 AI Candidate Ranking")

    with c2:
        st.success("📊 Analytics Dashboard")
        st.success("💬 Interview Questions")
        st.success("☁️ Deployment Ready")

    st.divider()

    st.info("🚀 Upload resumes and a Job Description to begin.")
    st.divider()

    st.subheader("📄 Step 1 : Upload Resume")

    show_upload_resume()

    st.divider()

    st.subheader("📝 Step 2 : Upload Job Description")

    show_job_description()

    st.divider()

    if (
        "resumes" in st.session_state
        and len(st.session_state["resumes"]) > 0
        and "jd_skills" in st.session_state
    ):

        st.success("✅ Resume and Job Description processed successfully!")

        st.info(
            "👉 Now open the **Candidate Ranking** page from the sidebar to view the results."
        )

    st.caption("© 2026 AI Resume Screening System")