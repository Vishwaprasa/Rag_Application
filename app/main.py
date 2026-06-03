from fastapi import FastAPI
from api.routes_rag import router as rag_router

app = FastAPI(title="RAG Application")

app.include_router(rag_router, prefix="/rag", tags=["RAG"])


@app.get("/")
def root():
    return {"message": "RAG API is running"}
