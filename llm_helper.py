import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()  # IMPORTANT

import streamlit as st
api_key = st.secrets.get("GROQ_API_KEY") or os.getenv("GROQ_API_KEY")
if not api_key:
    raise ValueError("GROQ_API_KEY is missing. Add it in Streamlit Cloud Secrets.")

client = Groq(api_key=api_key)


def get_ai_feedback(resume_text, job_desc, score):
    prompt = f"""
    You are an AI resume reviewer.

    Resume:
    {resume_text}

    Job Description:
    {job_desc}

    Match Score:
    {score}%

    Give:
    1. Feedback
    2. Improvements
    3. Suggested bullet points
    """

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content