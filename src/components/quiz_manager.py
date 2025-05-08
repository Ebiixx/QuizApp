class QuizManager:
    def __init__(self, api_client):
        self.api_client = api_client
        self.questions = []
        self.current_question_index = 0
        self.user_answers = []

    def fetch_questions(self, topic):
        self.questions = self.api_client.get_questions(topic)
        self.current_question_index = 0
        self.user_answers = []

    def get_current_question(self):
        if self.questions and self.current_question_index < len(self.questions):
            return self.questions[self.current_question_index]
        return None

    def submit_answer(self, answer):
        if self.current_question_index < len(self.questions):
            self.user_answers.append(answer)
            self.current_question_index += 1

    def validate_answers(self):
        correct_answers = [q['correct_answer'] for q in self.questions]
        score = sum(1 for i, answer in enumerate(self.user_answers) if answer == correct_answers[i])
        return score, len(self.questions)