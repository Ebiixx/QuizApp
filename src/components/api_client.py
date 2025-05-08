class APIClient:
    def __init__(self, api_key, endpoint):
        self.api_key = api_key
        self.endpoint = endpoint

    def generate_questions(self, topic, num_questions=5):
        import requests

        headers = {
            'Authorization': f'Bearer {self.api_key}',
            'Content-Type': 'application/json'
        }

        data = {
            'prompt': f'Generate {num_questions} questions about {topic}.',
            'max_tokens': 150
        }

        response = requests.post(self.endpoint, headers=headers, json=data)

        if response.status_code == 200:
            return response.json().get('choices', [{}])[0].get('text', '').strip().split('\n')
        else:
            raise Exception(f"Error: {response.status_code} - {response.text}")