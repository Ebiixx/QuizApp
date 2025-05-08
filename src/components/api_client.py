import os
from openai import AzureOpenAI
from dotenv import load_dotenv
import json

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

    def get_questions(self, topic, num_questions=20):
        """Generiert mehrere Quizfragen basierend auf dem Thema."""
        response = self.client.chat.completions.create(
            max_tokens=2000,
            model="gpt-4o-mini",  # Ersetze durch den richtigen Modellnamen oder Deployment-Namen
            messages=[
                {"role": "system", "content": "You are a helpful assistant that generates quiz questions."},
                {"role": "user", "content": f"Generate {num_questions} quiz questions about {topic} in JSON format. Each question should include a 'question', 'answers' (list of 4 options), and 'correct_answer'."}
            ]
        )

        # Die Antwort der API ist ein String. Wir müssen sie in ein Python-Objekt umwandeln.
        raw_text = response.choices[0].message.content.strip()

        # Debugging: API-Antwort ausgeben
        print("API Response:", raw_text)

        # JSON-Block extrahieren
        start_index = raw_text.find("[")
        end_index = raw_text.rfind("]") + 1
        if start_index == -1 or end_index == -1:
            raise ValueError("No valid JSON array found in the API response")

        json_text = raw_text[start_index:end_index]

        try:
            questions = json.loads(json_text)
        except json.JSONDecodeError as e:
            raise ValueError(f"Invalid JSON response: {str(e)}")

        return questions