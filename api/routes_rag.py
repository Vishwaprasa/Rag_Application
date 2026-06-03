from fastapi import APIRouter
from models.request_models import QueryRequest
from models.response_models import QueryResponse
from services.rag_orchestrator import RAGOrchestrator

router = APIRouter()
rag = RAGOrchestrator()


@router.post("/query", response_model=QueryResponse)
async def query_rag(request: QueryRequest):
    answer = await rag.run(request.query)
    return QueryResponse(answer=answer)
