import streamlit as st

from utils.preprocessing import clean_text
from utils.skill_extractor import extract_skills


def show_job_description():

    st.header("📄 Upload Job Description")

    jd_text = st.text_area(
        "Paste the Job Description here",
        height=300,
        placeholder="Paste the complete Job Description here..."
    )

    if st.button("Analyze Job Description"):

        if jd_text.strip() == "":
            st.warning("⚠ Please enter a Job Description.")
            return

        cleaned_jd = clean_text(jd_text)

        jd_skills = extract_skills(cleaned_jd)

        # Save in Session State
        st.session_state["jd_text"] = cleaned_jd
        st.session_state["jd_skills"] = jd_skills

        st.success("✅ Job Description Processed Successfully")

        with st.expander("📄 Original Job Description"):
            st.write(jd_text)

        with st.expander("🧹 Cleaned Job Description"):
            st.write(cleaned_jd)

        st.subheader("🎯 Required Skills")

        if jd_skills:

            cols = st.columns(3)

            for i, skill in enumerate(jd_skills):
                cols[i % 3].success(skill)

        else:
            st.warning("No skills found.")