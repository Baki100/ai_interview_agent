import spacy
import re
import random
from difflib import SequenceMatcher
from data_ingestion import load_data  # Import the data ingestion function

# Load spaCy model
nlp = spacy.load('en_core_web_md')  # Using medium model for better similarity judgments

# List of known technical terms to ensure they're captured
technical_terms = ['Python', 'R', 'SQL', 'TensorFlow', 'PyTorch', 'Machine Learning', 'Deep Learning', 'Data Analysis']

def similar(a: str, b: str) -> float:
    '''
    Determines the similarity ratio between two strings.

    Args:
        a (str): The first string to compare.
        b (str): The second string to compare.

    Returns:
        float: Similarity ratio between the two strings.
    '''
    return SequenceMatcher(None, a, b).ratio()

def extract_keywords_with_ner(text: str) -> list:
    '''
    Extracts key terms from a document using spaCy's Named Entity Recognition (NER).

    Args:
        text (str): The input text to extract keywords from.

    Returns:
        list: A list of extracted keywords.
    '''
    doc = nlp(text)
    keywords = []
    for ent in doc.ents:
        if ent.label_ in ['ORG', 'SKILL', 'WORK_OF_ART', 'PRODUCT']:
            keywords.append(ent.text)

    # Adding technical terms detection considering case sensitivity
    tokens = [chunk.text for chunk in doc.noun_chunks if any(term.lower() in chunk.text.lower() for term in technical_terms)]
    keywords.extend(tokens)

    return list(set(keywords))

def filter_similar_keywords(keywords: list, similarity_threshold: float = 0.8) -> list:
    '''
    Filters out similar keywords based on a similarity threshold.

    Args:
        keywords (list): A list of keywords to filter.
        similarity_threshold (float): The similarity threshold above which keywords are considered similar.

    Returns:
        list: A list of filtered keywords.
    '''
    base_keywords = []
    for keyword in keywords:
        if not any(similar(keyword.lower(), existing_keyword.lower()) > similarity_threshold for existing_keyword in base_keywords):
            base_keywords.append(keyword)
    return base_keywords

def generate_questions(keywords: list, job_title: str, core_values: list, context: str) -> list:
    '''
    Generates interview questions based on provided keywords, job title, and core values.

    Args:
        keywords (list): A list of keywords to include in the questions.
        job_title (str): The job title to ask about.
        core_values (list): A list of company's core values.
        context (str): The context for the questions (e.g., "job requirements").

    Returns:
        list: A list of generated interview questions.
    '''
    questions = [f"Can you describe your experience as a {job_title} and how it relates to our job requirements?"]  # Always ask about job title
    for keyword in keywords:
        questions.append(f"Can you describe your experience with {keyword} as it relates to our {context}?")
    for core_value in core_values:
        questions.append(f"How does our company's focus on {core_value} align with you?")
    questions = list(dict.fromkeys(questions))
    random.shuffle(questions)  # Randomize the questions
    return questions

def extract_job_title(text: str) -> str:
    '''
    Extracts the job title from the job post text using regex.

    Args:
        text (str): The input text to extract the job title from.

    Returns:
        str: The extracted job title.
    '''
    match = re.search(r'Job Title:\s*(.*)', text)
    if match:
        return match.group(1).strip()
    return "Unknown Job Title"

def extract_core_values(text: str) -> list:
    '''
    Extracts the core values from the company profile text using regex.

    Args:
        text (str): The input text to extract the core values from.

    Returns:
        list: A list of extracted core values.
    '''
    match = re.search(r'Core Values:\s*(.*)', text)
    if match:
        return [value.strip() for value in match.group(1).split(',')]
    return []

if __name__ == "__main__":
    # Load the data using the data ingestion function
    documents = load_data()

    job_keywords = extract_keywords_with_ner(documents['job_post'])
    resume_keywords = extract_keywords_with_ner(documents['candidate_resume'])

    # Filter technical terms present in both job post and resume
    common_technical_keywords = [term for term in technical_terms if term in job_keywords and term in resume_keywords]

    # Find common keywords between job post and resume
    common_keywords = set(job_keywords).intersection(set(resume_keywords))

    # Combine and filter similar keywords
    filtered_keywords = filter_similar_keywords(list(common_keywords) + common_technical_keywords)

    # Extract job title from job post
    job_title = extract_job_title(documents['job_post'])

    # Extract core values from company profile
    core_values = extract_core_values(documents['company_profile'])

    # Print keywords for debugging
    print("Filtered Keywords: ", filtered_keywords)
    print("Job Title: ", job_title)
    print("Core Values: ", core_values)

    interview_questions = generate_questions(filtered_keywords, job_title, core_values, "job requirements")

    # Print questions for debugging
    print("Generated Questions: ")
    for i, question in enumerate(interview_questions, 1):
        print(f"{i}. {question}")
