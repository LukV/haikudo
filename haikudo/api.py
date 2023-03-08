import os
import openai
from dotenv import load_dotenv

load_dotenv()

# Load your API key from an environment variable or 
# secret management service
openai.api_key = os.getenv("OPENAI_API_KEY")

def call_api(prompt):
    model_engine = "text-davinci-002"
    max_tokens = 150
    completion = openai.Completion.create(
        engine=model_engine,
        prompt=prompt
    )
    return completion.choices[0].text
