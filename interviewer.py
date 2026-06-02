import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

genai.configure(
    api_key=os.getenv("GEMINI_API_KEY")
)

model = genai.GenerativeModel("gemini-2.5-flash")


def generate_questions(resume_text):

    prompt = f"""
    You are an HR interviewer.

    Read the resume and generate exactly 5 interview questions.

    Rules:
    - One question per line
    - No numbering
    - No bullets
    - Only questions

    Resume:
    {resume_text}
    """

    response = model.generate_content(prompt)

    questions = response.text.strip().split("\n")

    questions = [
        q.strip("-*1234567890. ")
        for q in questions
        if q.strip()
    ]

    return questions