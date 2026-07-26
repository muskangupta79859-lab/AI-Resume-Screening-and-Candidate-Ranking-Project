import plotly.express as px
from collections import Counter
import pandas as pd
import streamlit as st
from utils.matching import calculate_match
from utils.interview_generator import generate_questions
from utils.pdf_generator import create_candidate_pdf
from utils.predictor import predict_candidate
from database.database import save_candidate


def show_candidate_ranking():

    st.header("🏆 Candidate Ranking")

    # Check Job Description
    if "jd_skills" not in st.session_state:

        st.warning("⚠ Please upload and analyze the Job Description first.")
        return

    # Check Resume
    if "resumes" not in st.session_state or len(st.session_state["resumes"]) == 0:

        st.warning("⚠ Please upload resumes first.")
        return

    results = []

    jd_skills = st.session_state["jd_skills"]
    with st.spinner("🔍 AI is analyzing resumes..."):

        for resume in st.session_state["resumes"]:

            matched, missing, score = calculate_match(
                resume["skills"],
                jd_skills
            )

            prediction = predict_candidate(
                score,
                len(matched),
                len(missing)
            )

            results.append({
                "Candidate": resume["name"],
                "Match %": score,
                "Matched Skills": matched,
                "Missing Skills": missing,
                "Prediction": prediction
            })

    for resume in st.session_state["resumes"]:

        matched, missing, score = calculate_match(
            resume["skills"],
            jd_skills
        )
        prediction=predict_candidate(
            score,
            len(matched),
            len(missing)
        )
        results.append({
            "Candidate": resume["name"],
            "Match %": score,
            "Matched Skills": matched,
            "Missing Skills": missing,
            "Prediction": prediction
        })

    results = sorted(
        results,
        key=lambda x: x["Match %"],
        reverse=True
    )
    ranking_df = pd.DataFrame(results)

    ranking_df.insert(
        0,
        "Rank",
        range(1, len(ranking_df)+1)
    )
    st.subheader("🔍 Search & Filter Candidates")
    search_name = st.text_input(
        "Search by Candidate Name",
        ""
    )
    min_score = st.slider(
        "Minimum Match Score (%)",
        0,
        100,
        0
    )
    filtered_df = ranking_df.copy()


    if search_name:

        filtered_df = filtered_df[
            filtered_df["Candidate"]
            .str.contains(
                search_name,
                case=False
            )
        ]


    filtered_df = filtered_df[
        filtered_df["Match %"] >= min_score
    ]
    st.dataframe(
        filtered_df,
        use_container_width=True
    )
    st.header("📊 Analytics Dashboard")
    col1, col2, col3 = st.columns(3)

    col1.metric(
        "👥 Total Candidates",
        len(ranking_df)
    )

    col2.metric(
        "⭐ Highest Match",
        f"{ranking_df['Match %'].max()}%"
    )

    col3.metric(
        "📊 Average Match",
        f"{ranking_df['Match %'].mean():.1f}%"
    )

    fig = px.histogram(
        ranking_df,
        x="Match %",
        nbins=10,
        title="Match Score Distribution"
    )

    st.plotly_chart(fig, use_container_width=True)
    fig = px.bar(
        ranking_df,
        x="Candidate",
        y="Match %",
        color="Match %",
        title="Candidate Ranking"
    )

    st.plotly_chart(fig, use_container_width=True)
    prediction_count = ranking_df["Prediction"].value_counts()

    fig = px.pie(
        values=prediction_count.values,
        names=prediction_count.index,
        title="Prediction Distribution"
    )

    st.plotly_chart(fig, use_container_width=True)
    all_skills = []

    for skills in ranking_df["Matched Skills"]:
        all_skills.extend(skills)

    skill_count = Counter(all_skills)

    skill_df = pd.DataFrame(
        skill_count.items(),
        columns=["Skill", "Count"]
    )

    fig = px.bar(
        skill_df.sort_values("Count", ascending=False),
        x="Skill",
        y="Count",
        title="Top Matched Skills"
    )

    st.plotly_chart(fig, use_container_width=True)

    st.balloons()

    st.success("🎉 AI Candidate Ranking Generated Successfully!")
    
    csv = ranking_df.to_csv(index=False)

    st.download_button(
        label="📤 Export Ranking CSV",
        data=csv,
        file_name="candidate_ranking.csv",
        mime="text/csv"
    )

    medals = ["🥇", "🥈", "🥉"]

    for i, candidate in enumerate(filtered_df.to_dict("records")):

        rank = medals[i] if i < 3 else f"{i+1}."

        with st.container():

            col1, col2 = st.columns([4,1])

            with col1:

                st.subheader(f"{rank} {candidate['Candidate']}")

                st.progress(int(candidate["Match %"]))

                st.write(f"**Matched Skills:** {', '.join(candidate['Matched Skills'])}")

                if candidate["Missing Skills"]:
                    st.write(f"**Missing Skills:** {', '.join(candidate['Missing Skills'])}")
                else:
                    st.success("No Missing Skills 🎉")

            with col2:

                st.metric("Match", f"{candidate['Match %']}%")
                prediction = predict_candidate(
                    candidate["Match %"],
                    len(candidate["Matched Skills"]),
                    len(candidate["Missing Skills"])
                )

                if prediction == "Highly Suitable":
                    st.success("🟢 Highly Suitable")

                elif prediction == "Suitable":
                    st.info("🔵 Suitable")

                elif prediction == "Moderately Suitable":
                    st.warning("🟡 Moderately Suitable")

                else:
                    st.error("🔴 Not Suitable")
                
                # PDF Report

                if st.button(
                    "📄 Generate Report",
                    key=f"pdf_{i}"
                ):

                    pdf_file = create_candidate_pdf(candidate)

                    with open(pdf_file,"rb") as file:

                        st.download_button(
                            label="⬇ Download PDF",
                            data=file,
                            file_name=f"{candidate['Candidate']}_report.pdf",
                            mime="application/pdf",
                            key=f"download_{i}"
                    )
                save_candidate(
                    candidate["Candidate"],
                    candidate["Match %"],
                    prediction,
                    candidate["Matched Skills"],
                    candidate["Missing Skills"]
            )

                questions = generate_questions(candidate["Matched Skills"])

                if questions:

                    with st.expander("💬 Interview Questions"):

                        for skill, ques in questions.items():

                            st.markdown(f"### {skill}")

                            for q in ques:
                                st.write("•", q)
            st.divider()