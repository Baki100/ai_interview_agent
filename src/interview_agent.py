import random

class AIInterviewAgent:
    def __init__(self, questions):
        self.questions = questions
        self.responses = []
        self.current_question = 0

    def ask_next_question(self):
        '''
        Asks the next question in the sequence.

        Returns:
            str: The next interview question or a concluding statement if all questions have been asked.
        '''
        if self.current_question < len(self.questions):
            question = self.questions[self.current_question]
            self.current_question += 1
            return question
        else:
            return "Thank you for your time. This concludes our interview."

    def record_response(self, response):
        '''
        Records the candidate's response.

        Args:
            response (str): The candidate's response to the current question.
        '''
        self.responses.append(response)

    def save_responses(self, file_name):
        '''
        Saves the recorded responses to a text file along with their corresponding questions.

        Args:
            file_name (str): The name of the file to save the responses.
        '''
        with open(file_name, 'w') as file:
            for i, response in enumerate(self.responses):
                question = self.questions[i] if i < len(self.questions) else "End of Interview"
                file.write(f"Q: {question}\nA: {response}\n\n")

    def conduct_interview(self):
        '''
        Conducts the interview by asking questions and recording responses.
        '''
        print("Interview Start\n")
        while self.current_question < len(self.questions):
            question = self.ask_next_question()
            print(question)
            response = input("Candidate Response: ")
            self.record_response(response)
        print("Thank you for your time. This concludes our interview.")
        print("Interview End\n")

        # Save responses to a text file
        self.save_responses('interview_responses.txt')

        # Print all recorded responses
        print("All Responses Recorded: ")
        for i, response in enumerate(self.responses, 1):
            print(f"{i}. {response}")

if __name__ == "__main__":
    from question_generation import generate_questions, extract_keywords_with_ner, filter_similar_keywords, extract_job_title, extract_core_values
    from data_ingestion import load_data

    # Load the data using the data ingestion function
    documents = load_data()

    job_keywords = extract_keywords_with_ner(documents['job_post'])
    resume_keywords = extract_keywords_with_ner(documents['candidate_resume'])
    common_keywords = set(job_keywords).intersection(set(resume_keywords))
    filtered_keywords = filter_similar_keywords(list(common_keywords))
    job_title = extract_job_title(documents['job_post'])
    core_values = extract_core_values(documents['company_profile'])

    # Generate interview questions using the question generation script
    interview_questions = generate_questions(filtered_keywords, job_title, core_values, "job requirements")
    random.shuffle(interview_questions)  # Randomize the questions

    agent = AIInterviewAgent(interview_questions)
    agent.conduct_interview()
