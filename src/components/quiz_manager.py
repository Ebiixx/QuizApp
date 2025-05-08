class QuizManager:
    def __init__(self, api_client):
        self.api_client = api_client

    def fetch_questions(self, topic, num_questions=20):
        """Ruft mehrere Fragen und Antworten basierend auf dem Thema ab."""
        response = self.api_client.get_questions(topic, num_questions)

        # Beispiel für die Verarbeitung der API-Antwort
        # Erwarte eine Liste von Fragen
        questions = []
        for item in response:
            questions.append({
                "question": item.get("question", "No question available."),
                "answers": item.get("answers", ["Option 1", "Option 2", "Option 3", "Option 4"]),
                "correct_answer": item.get("correct_answer", "Option 1")
            })
        return questions