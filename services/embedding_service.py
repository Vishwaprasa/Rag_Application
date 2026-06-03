from openai import OpenAI
from app.config import OPENAI_API_KEY, EMBEDDING_MODEL
import numpy as np


class EmbeddingService:
    def __init__(self):
        if not OPENAI_API_KEY:
            self.client = None
        else:
            self.client = OpenAI(api_key=OPENAI_API_KEY)

    def embed(self, text: str):
        # Dev fallback: return deterministic pseudo-embedding when no API key
        if self.client is None:
            vec = np.zeros(1536, dtype="float32")
            vec[0] = float(len(text))
            return vec.tolist()

        response = self.client.embeddings.create(model=EMBEDDING_MODEL, input=text)
        return response.data[0].embedding
