class QuizManager:
    def __init__(self, api_client):
        self.api_client = api_client

    def fetch_questions(self, topic):
        """Ruft eine Frage und Antworten basierend auf dem Thema ab."""
        response = self.api_client.get_questions(topic)

        # Beispiel für die Verarbeitung der API-Antwort
        # Stelle sicher, dass die API-Antwort ein JSON-ähnliches Format hat
        return {
            "question": response.get("question", "No question available."),
            "answers": response.get("answers", ["Option 1", "Option 2", "Option 3", "Option 4"]),
            "correct_answer": response.get("correct_answer", "Option 1")
        }