# AI Interview With Talent (POC)

## Project Overview
This project demonstrates an AI Interview Agent that conducts interviews based on a given job post, company profile, and candidate resume.

## Repository Structure
interview_venv/ # Virtual environment directory

├── include/ # Virtual environment include files

├── lib/ # Virtual environment libraries

├── Scripts/ # Virtual environment scripts

data/ # Directory for storing data files

├── company_profile.txt # Company profile (mission, vision, values)

├── candidate_resume.txt # Candidate resume

└── job_post.txt # Job post describing the position

src/ # Directory for source code

├── data_ingestion.py # Script for loading and ingesting data

├── question_generation.py # Script for generating interview questions

├── interview_agent.py # Main script for simulating the interview process

└── voice_interview_agent.py # Optional: Script for voice-based interview agent

README.md # Project documentation

requirements.txt # Dependencies and libraries for the project


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

3. **Run the command**:
   ```bash
   python -m spacy download en_core_web_md
   ```

3. **Run the interview agent script**:
    ```bash
    cd interview_venv
    python src/interview_agent.py
    ```

4. **Run the voice interview agent script** (optional):
    ```bash
    cd interview_venv
    python src/voice_interview_agent.py
    ```

