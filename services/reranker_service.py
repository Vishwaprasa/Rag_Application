import numpy as np


class RerankerService:
    def rerank(self, query_embedding, docs):
        scored = []

        for doc in docs:
            emb = np.array(doc["embedding"])
            score = np.dot(query_embedding, emb) / (
                np.linalg.norm(query_embedding) * np.linalg.norm(emb)
            )
            scored.append((score, doc))

        scored.sort(reverse=True, key=lambda x: x[0])

        return [doc for _, doc in scored]
