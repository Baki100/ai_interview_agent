import pyttsx3
import speech_recognition as sr
import random
from interview_agent import AIInterviewAgent  # Import the base interview agent

class VoiceAIInterviewAgent(AIInterviewAgent):
    def __init__(self, questions):
        super().__init__(questions)
        self.engine = pyttsx3.init()
        self.recognizer = sr.Recognizer()
        self.microphone = sr.Microphone()

    def speak(self, text):
        '''
        Converts text to speech and speaks it out.

        Args:
            text (str): The text to be converted to speech.
        '''
        self.engine.say(text)
        self.engine.runAndWait()

    def listen(self):
        '''
        Listens to the candidate's response and converts speech to text.

        Returns:
            str: The candidate's response as text.
        '''
        with self.microphone as source:
            print("Listening...")
            audio = self.recognizer.listen(source)
        try:
            response = self.recognizer.recognize_google(audio)
            print(f"Candidate Response: {response}")
            return response
        except sr.UnknownValueError:
            self.speak("Sorry, I did not catch that. Could you please repeat?")
            return self.listen()
        except sr.RequestError:
            self.speak("Sorry, there seems to be an issue with the speech recognition service.")
            return ""

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
        Conducts the interview by asking questions and recording responses using voice.
        '''
        self.speak("Interview Start")
        while self.current_question < len(self.questions):
            question = self.ask_next_question()
            self.speak(question)
            response = self.listen()
            self.record_response(response)
        self.speak("Thank you for your time. This concludes our interview.")
        self.speak("Interview End")

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

    agent = VoiceAIInterviewAgent(interview_questions)
    agent.conduct_interview()
