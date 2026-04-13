
import os
from openai import OpenAI
from dotenv import load_dotenv
from llm.base import LLMProvider

load_dotenv()

class OpenAIClient(LLMProvider):

    def __init__(self):
        self.client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    def call(self, prompt: str) -> str:
        response = self.client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.2,
        )
        return response.choices[0].message.content.strip()
