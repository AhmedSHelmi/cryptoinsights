import openai

class GPTService:
    def __init__(self, api_key):
        openai.api_key = api_key

    def get_recommendations(self, prompt):
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=150
        )
        return response.choices[0].text.strip()
