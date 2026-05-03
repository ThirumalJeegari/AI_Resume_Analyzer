import streamlit as st
from resume_parser import extract_text_from_pdf
from matcher import calculate_match_score, extract_skills
from llm_helper import get_ai_feedback
import os
from dotenv import load_dotenv

load_dotenv()

st.set_page_config(page_title="AI Resume Analyzer", layout="wide")

st.title("📄 AI Resume Analyzer")
st.write("Upload your resume and compare it with a job description")

# Upload resume
resume_file = st.file_uploader("Upload Resume (PDF)", type=["pdf"])

# Job description
job_desc = st.text_area("Paste Job Description")

if st.button("Analyze Resume"):

    if resume_file and job_desc:
        with st.spinner("Analyzing..."):

            resume_text = extract_text_from_pdf(resume_file)

            # Skill extraction
            resume_skills = extract_skills(resume_text)
            job_skills = extract_skills(job_desc)

            # Match score
            score = calculate_match_score(resume_skills, job_skills)

            # AI feedback
            feedback = get_ai_feedback(resume_text, job_desc, score)

            st.subheader("📊 Match Score")
            st.success(f"{score}% Match with Job Description")

            st.subheader("🧠 AI Feedback")
            st.write(feedback)

            st.subheader("🧾 Extracted Resume Text")
            st.text(resume_text[:2000])

    else:
        st.error("Please upload resume and job description")