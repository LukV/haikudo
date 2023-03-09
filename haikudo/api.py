import os
import openai
from dotenv import load_dotenv
import asyncio
from storage import write_response

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

async def call_api(topic, mood):
    model_engine = "text-davinci-002"
    max_tokens = 150
    completion = openai.Completion.create(
        engine=model_engine,
        prompt=f"Write a {mood} haiku about {topic}"
    )
    response = completion.choices[0].text
    asyncio.create_task(write_response(response, topic))
    return response
