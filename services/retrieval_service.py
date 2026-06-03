from db.vector_db import VectorDB
from services.embedding_service import EmbeddingService


class RetrievalService:
    def __init__(self):
        self.db = VectorDB()
        self.embedder = EmbeddingService()

    def retrieve(self, query: str, k: int = 3):
        query_embedding = self.embedder.embed(query)
        results = self.db.search(query_embedding, k=k)
        return results
