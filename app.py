import streamlit as st
from streamlit_option_menu import option_menu

from utils.parser import extract_resume_text
from utils.skill_extractor import extract_skills
from utils.preprocessing import clean_text
from utils.matching import calculate_match
from utils.pdf_generator import create_candidate_pdf

from views.candidate_ranking import show_candidate_ranking
from views.home import show_home
from views.upload_resume import show_upload_resume
from views.job_description import show_job_description
from views.analytics import show_analytics


st.set_page_config(
    page_title="AI Resume Screening & Candidate Ranking",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

def load_css():
    with open("assets/style.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_css()
# Sidebar
with st.sidebar:
    selected = option_menu(
        "Navigation",
        [
            "Home",
            "Candidate Ranking",
            "Analytics",
            "About"
        ],
        icons=[
            "house",
            "people",
            "bar-chart",
            "info-circle"
        ],
        default_index=0,
    )

# Home Page
if selected == "Home":
    show_home()
# Candidate Ranking Page
elif selected == "Candidate Ranking":
    show_candidate_ranking()
# Analytics Page
elif selected == "Analytics":
    show_analytics()
# About Page
elif selected == "About":

    st.header("About Project")

    st.write("""
    AI Resume Screening System

    Technologies:

    • Machine Learning

    • NLP

    • Deep Learning

    • Streamlit

    • SQLite
    """)

