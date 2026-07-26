import streamlit as st

from utils.parser import extract_resume_text
from utils.preprocessing import clean_text
from utils.skill_extractor import extract_skills


def show_upload_resume():

    st.header("📂 Upload Candidate Resume")

    uploaded_files = st.file_uploader(
        "Upload PDF or DOCX resumes",
        type=["pdf", "docx"],
        accept_multiple_files=True
    )

    if uploaded_files:

        if "resumes" not in st.session_state:
            st.session_state["resumes"] = []

        # Clear previous uploads
        st.session_state["resumes"] = []

        for file in uploaded_files:

            st.subheader(file.name)

            text = extract_resume_text(file)
            cleaned_text = clean_text(text)
            skills = extract_skills(cleaned_text)

            st.session_state["resumes"].append({
                "name": file.name,
                "skills": skills,
                "text": cleaned_text
            })

            st.success("✅ Resume Processed Successfully")

            with st.expander("📄 Original Resume"):
                st.write(text)

            with st.expander("🧹 Cleaned Resume"):
                st.write(cleaned_text)

            st.subheader("🎯 Extracted Skills")

            if skills:

                cols = st.columns(3)

                for i, skill in enumerate(skills):
                    cols[i % 3].success(skill)

            else:
                st.warning("No skills found.")