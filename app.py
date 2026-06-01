import streamlit as st
import pdfplumber
import ollama

st.set_page_config(page_title="SmartHire AI Agent", page_icon="🤖")

MODEL_NAME = "llama3.2:3b"

def extract_text_from_pdf(uploaded_file):
    text = ""
    with pdfplumber.open(uploaded_file) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"
    return text

def analyze_resume(job_description, resume_text):
    prompt = f"""
You are SmartHire AI Agent, an AI resume screening assistant.

Compare the resume with the job description.

Return the answer in this format:

Candidate Match Score: __/100

Decision:
Shortlist / Human Review / Reject

Reason:
Explain clearly.

Matched Skills:
- skill 1
- skill 2

Missing Skills:
- skill 1
- skill 2

Recruiter Summary:
Write a short professional summary.

Human Escalation:
Mention if this case should go to human review and why.

Job Description:
{job_description}

Resume:
{resume_text}
"""

    response = ollama.chat(
        model=MODEL_NAME,
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return response["message"]["content"]

st.title("SmartHire AI Agent")
st.write("Free Local AI Resume Screening Agent using Ollama")

job_description = st.text_area("Paste Job Description", height=200)

resume_file = st.file_uploader("Upload Resume PDF", type=["pdf"])

if st.button("Analyze Candidate"):
    if not job_description:
        st.error("Please paste the job description.")
    elif not resume_file:
        st.error("Please upload a resume PDF.")
    else:
        with st.spinner("Reading resume..."):
            resume_text = extract_text_from_pdf(resume_file)

        with st.spinner("Local AI is analyzing the candidate..."):
            result = analyze_resume(job_description, resume_text)

        st.subheader("AI Screening Result")
        st.write(result)

        with st.expander("View Extracted Resume Text"):
            st.text_area("Resume Text", resume_text, height=300)