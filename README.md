File Structure

rag_app/
│
├── app/
│   ├── main.py                  # FastAPI entry
│   ├── config.py                # settings (env, keys)
│
│   ├── api/                     # routes
│   │   ├── routes_rag.py
│   │   └── routes_auth.py
│
│   ├── services/                # core logic
│   │   ├── embedding_service.py
│   │   ├── retrieval_service.py
│   │   ├── reranker_service.py
│   │   ├── llm_service.py
│   │   └── rag_orchestrator.py
│
│   ├── ingestion/               # offline pipeline
│   │   ├── loader.py
│   │   ├── preprocess.py
│   │   ├── chunker.py
│   │   └── indexer.py
│
│   ├── db/
│   │   ├── vector_db.py         # FAISS / Pinecone
│   │   └── metadata_db.py       # Mongo/Postgres
│
│   ├── models/                  # schemas
│   │   ├── request_models.py
│   │   └── response_models.py
│
│   ├── utils/
│   │   ├── logger.py
│   │   └── helpers.py
│
│   └── core/
│       ├── prompts.py           # prompt templates
│       └── constants.py
│
├── scripts/
│   └── run_ingestion.py         # run indexing pipeline
│
├── tests/
│
├── .env
├── requirements.txt
└── README.md