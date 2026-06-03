from services.retrieval_service import RetrievalService
from services.llm_services import LLMService
from services.reranker_service import RerankerService
from utils.helpers import format_docs


class RAGOrchestrator:
    def __init__(self):
        self.retriever = RetrievalService()
        self.reranker = RerankerService()
        self.llm = LLMService()

    async def run(self, query: str):
        docs = self.retriever.retrieve(query)

        # optional rerank
        # docs = self.reranker.rerank(query_embedding, docs)

        context = format_docs(docs)

        prompt = f"""
        Answer ONLY from the context.

        Context:
        {context}

        Question:
        {query}
        """

        return self.llm.generate(prompt)
