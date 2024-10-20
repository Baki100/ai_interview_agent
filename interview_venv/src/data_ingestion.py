import os

def load_data(data_dir=os.path.join(os.path.dirname(__file__), '..', 'data')):
    job_post_file = os.path.join(data_dir, 'job_post.txt')
    company_profile_file = os.path.join(data_dir, 'company_profile.txt')
    candidate_resume_file = os.path.join(data_dir, 'candidate_resume.txt')

    with open(job_post_file, 'r') as file:
        job_post = file.read().strip()

    with open(company_profile_file, 'r') as file:
        company_profile = file.read().strip()

    with open(candidate_resume_file, 'r') as file:
        candidate_resume = file.read().strip()

    documents = {
        'job_post': job_post,
        'company_profile': company_profile,
        'candidate_resume': candidate_resume
    }

    return documents

if __name__ == "__main__":
    documents = load_data()
    print("Data Ingestion Complete: ", documents.keys())

    for key, value in documents.items():
        print(f"---- {key.upper()} ----")
        print(value)
        print("\n")



