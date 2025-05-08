import os
from openai import AzureOpenAI
from dotenv import load_dotenv

# .env-Datei laden
load_dotenv()

class APIClient:
    def __init__(self):
        # Azure OpenAI-Client konfigurieren
        self.client = AzureOpenAI(
            azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
            api_key=os.getenv("AZURE_OPENAI_API_KEY"),
            api_version="2024-02-01"  # Beispiel: API-Version anpassen
        )

    def get_questions(self, topic):
        """Generiert Quizfragen basierend auf dem Thema."""
        response = self.client.chat.completions.create(
            max_tokens=100,
            model="gpt-4o-mini",  # Ersetze durch den richtigen Modellnamen oder Deployment-Namen
            messages=[
                {"role": "system", "content": "You are a helpful assistant that generates quiz questions."},
                {"role": "user", "content": f"Generate a quiz question about {topic}."}
            ]
        )

        # Die Antwort der API ist ein String. Wir müssen sie in ein Dictionary umwandeln.
        raw_text = response.choices[0].message.content.strip()

        # Beispiel: Die API sollte eine strukturierte Antwort zurückgeben.
        # Wir simulieren hier die Verarbeitung der Antwort.
        # Ersetze dies durch die tatsächliche Logik, falls die API anders antwortet.
        question_data = {
            "question": "What is the capital of France?",
            "answers": ["Berlin", "Madrid", "Paris", "Rome"],
            "correct_answer": "Paris"
        }

        # Falls die API bereits ein JSON-ähnliches Format zurückgibt, kannst du `json.loads` verwenden:
        # import json
        # question_data = json.loads(raw_text)

        return question_data