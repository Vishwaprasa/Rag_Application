from openai import OpenAI
from app.config import OPENAI_API_KEY, LLM_MODEL


class LLMService:
    def __init__(self):
        if not OPENAI_API_KEY:
            self.client = None
        else:
            self.client = OpenAI(api_key=OPENAI_API_KEY)

    def generate(self, prompt: str):
        # Dev fallback: return canned response when no API key
        if self.client is None:
            return "[dev-mode] Mock answer: unable to call OpenAI. Answer based on provided context."

        response = self.client.chat.completions.create(
            model=LLM_MODEL,
            messages=[{"role": "user", "content": prompt}],
            temperature=0.3,
        )
        return response.choices[0].message.content
