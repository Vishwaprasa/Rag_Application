from services.embedding_service import EmbeddingService
from db.vector_db import VectorDB


class Indexer:
    def __init__(self):
        self.embedder = EmbeddingService()
        self.db = VectorDB()

    def index(self, chunks):
        embeddings = [self.embedder.embed(chunk) for chunk in chunks]
        self.db.add(embeddings, chunks)
