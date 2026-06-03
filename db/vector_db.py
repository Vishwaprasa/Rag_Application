import faiss
import numpy as np
import os
import pickle
from app.config import VECTOR_DB_PATH


class VectorDB:
    def __init__(self):
        self.index = None
        self.texts = []
        self._load()

    def _load(self):
        if os.path.exists(VECTOR_DB_PATH):
            self.index = faiss.read_index(VECTOR_DB_PATH)
            with open("data/texts.pkl", "rb") as f:
                self.texts = pickle.load(f)
        else:
            self.index = faiss.IndexFlatL2(1536)

    def save(self):
        faiss.write_index(self.index, VECTOR_DB_PATH)
        with open("data/texts.pkl", "wb") as f:
            pickle.dump(self.texts, f)

    def add(self, embeddings, texts):
        self.index.add(np.array(embeddings).astype("float32"))
        self.texts.extend(texts)
        self.save()

    def search(self, query_embedding, k=3):
        if self.index is None or self.index.ntotal == 0:
            return []

        D, I = self.index.search(np.array([query_embedding]).astype("float32"), k)

        results = []
        for idx in I[0]:
            if idx is None:
                continue
            if idx < 0 or idx >= len(self.texts):
                continue
            results.append({"text": self.texts[idx]})

        return results
