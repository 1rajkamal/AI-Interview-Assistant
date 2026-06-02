import streamlit as st
from resume_parser import extract_text
from interviewer import generate_questions
from scorer import evaluate_answer

st.title("🎤 AI Interview Assistant")

uploaded_file = st.file_uploader(
    "Upload Resume",
    type=["pdf"]
)

if uploaded_file:

    resume_text = extract_text(uploaded_file)

    if "questions" not in st.session_state:

        if st.button("Generate Interview Questions"):

            questions = generate_questions(resume_text)

            st.session_state.questions = questions
            st.session_state.current = 0
            st.session_state.scores = []

            st.rerun()

    if "questions" in st.session_state:

        questions = st.session_state.questions
        current = st.session_state.current

        total = len(questions)

        progress = current / total
        st.progress(progress)

        if current < total:

            st.subheader(
                f"Question {current+1} of {total}"
            )

            st.write(
                questions[current]
            )

            answer = st.text_area(
                "Your Answer",
                key=f"answer_{current}"
            )

            if st.button("Evaluate Answer"):

                feedback = evaluate_answer(
                    questions[current],
                    answer
                )

                st.session_state.feedback = feedback

        if "feedback" in st.session_state:

            st.subheader("AI Feedback")

            st.write(
                st.session_state.feedback
            )

            if st.button("Next Question"):

                st.session_state.current += 1

                if "feedback" in st.session_state:
                    del st.session_state.feedback

                st.rerun()

        if current >= total:

            st.success(
                "🎉 Interview Completed"
            )

            st.balloons()