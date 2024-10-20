# AI Interview Agent POC

## Project Overview
This project demonstrates an AI Interview Agent that conducts interviews based on a given job post, company profile, and candidate resume.

## Repository Structure
├── /interview_venv # Virtual environment directory │ 
├── /data # Directory for storing data files │ │ ├── company_profile.txt │ │ ├── candidate_resume.txt │ │ └── job_post.txt │ 
├── /src # Directory for source code │ │ ├── data_ingestion.py │ │ ├── question_generation.py │ │ ├── interview_agent.py │ │ └── voice_interview_agent.py │ 
├── /include # Virtual environment include files │ 
├── /lib # Virtual environment libraries │ 
└── /Scripts # Virtual environment scripts 
├── README.md # Project documentation 
├── requirements.txt # Dependencies


## How to Run
1. **Set up the virtual environment**:
    ```bash
    python -m venv interview_venv
    source interview_venv/bin/activate  # On Windows, use `interview_venv\Scripts\activate`
    ```

2. **Install the necessary dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

3. **Run the data ingestion script**:
    ```bash
    python src/data_ingestion.py
    ```

4. **Run the question generation script**:
    ```bash
    python src/question_generation.py
    ```

5. **Run the interview agent script**:
    ```bash
    python src/interview_agent.py
    ```

6. **Run the voice interview agent script** (optional):
    ```bash
    python src/voice_interview_agent.py
    ```

