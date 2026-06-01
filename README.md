# SmartHire AI Agent

SmartHire AI Agent is a free local AI resume screening web app built with Streamlit and Ollama.

It helps recruiters compare a candidate resume with a job description and generates:

* Candidate match score
* Shortlist / Human Review / Reject decision
* Matched skills
* Missing skills
* Recruiter summary
* Human escalation reason

## Important Note

This project currently works **locally** because it uses Ollama to run the AI model on the user's own computer.

It is not deployed on Streamlit Cloud because Streamlit Cloud does not run a local Ollama model server by default.

For evaluation, please run the project locally using the steps below.

## Tech Stack

* Python
* Streamlit
* pdfplumber
* Ollama
* Llama 3.2 3B local model

## How to Run Locally

### 1. Clone the Repository

```bash
git clone https://github.com/aimslab0/smart-hire-ai-agent.git
cd smart-hire-ai-agent
```

### 2. Install Python Dependencies

```bash
pip install -r requirements.txt
```

### 3. Install Ollama

Download and install Ollama from:

```text
https://ollama.com
```

### 4. Download Local AI Model

```bash
ollama pull llama3.2:3b
```

### 5. Run the App

```bash
streamlit run app.py
```

## Workflow

```text
Upload Resume PDF
        ↓
Extract Resume Text
        ↓
Paste Job Description
        ↓
Local LLM Analysis
        ↓
Generate Score + Decision + Summary
```

## Project Goal

The goal of this project is to automate the repetitive first screening stage of recruitment while keeping uncertain cases for human review.

This follows a human-in-the-loop approach where AI handles routine analysis and humans make final decisions when needed.
