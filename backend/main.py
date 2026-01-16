import os
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional, List

from rag.pdf_to_text import pdf_to_text
from rag.chunking import chunk_text
from rag.embed_store import build_and_save_index, load_index
from rag.rag_answer import retrieve, generate_answer

# Initialize FastAPI app
app = FastAPI(
    title="Insurance RAG Chatbot API",
    description="RAG-based chatbot for insurance customer support",
    version="1.0.0"
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, specify your frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Define paths
DATA_DIR = os.path.join(os.path.dirname(__file__), "data")
PDF_PATH = os.path.join(DATA_DIR, "knowledge.pdf")
INDEX_PATH = os.path.join(DATA_DIR, "index.faiss")
META_PATH = os.path.join(DATA_DIR, "chunks.json")

# Global variables for index and chunks
index = None
chunks = None

# Request/Response models
class ChatRequest(BaseModel):
    message: str

class ChatResponse(BaseModel):
    answer: str
    sources: Optional[List[str]] = None

class IngestResponse(BaseModel):
    status: str
    chunks: int
    message: str

@app.get("/")
def read_root():
    """Health check endpoint"""
    return {
        "status": "ok",
        "message": "Insurance RAG Chatbot API is running",
        "endpoints": {
            "ingest": "POST /ingest - Process PDF and build knowledge base",
            "chat": "POST /chat - Ask questions to the chatbot"
        }
    }

@app.post("/ingest", response_model=IngestResponse)
def ingest():
    """
    Ingest PDF and build the knowledge base index.
    This should be called once when setting up or updating the knowledge base.
    """
    global index, chunks
    
    try:
        # Check if PDF exists
        if not os.path.exists(PDF_PATH):
            raise HTTPException(
                status_code=404,
                detail=f"PDF not found at {PDF_PATH}. Please add a knowledge.pdf file."
            )
        
        print(f"Reading PDF from {PDF_PATH}...")
        text = pdf_to_text(PDF_PATH)
        
        print(f"Chunking text...")
        chunks = chunk_text(text, chunk_tokens=450, overlap_tokens=80)
        
        print(f"Building and saving index...")
        build_and_save_index(chunks, INDEX_PATH, META_PATH)
        
        print(f"Loading index...")
        index, chunks = load_index(INDEX_PATH, META_PATH)
        
        return IngestResponse(
            status="success",
            chunks=len(chunks),
            message=f"Successfully ingested PDF and created {len(chunks)} chunks"
        )
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Ingestion failed: {str(e)}")

@app.post("/chat", response_model=ChatResponse)
def chat(payload: ChatRequest):
    """
    Chat endpoint - answer questions based on the knowledge base.
    """
    global index, chunks
    
    # Check if index is loaded
    if index is None or chunks is None:
        # Try to load from disk
        if os.path.exists(INDEX_PATH) and os.path.exists(META_PATH):
            try:
                print("Loading index from disk...")
                index, chunks = load_index(INDEX_PATH, META_PATH)
            except Exception as e:
                raise HTTPException(
                    status_code=503,
                    detail="Knowledge base not ready. Please call /ingest first."
                )
        else:
            raise HTTPException(
                status_code=503,
                detail="Knowledge base not ingested yet. Please call /ingest first."
            )
    
    try:
        # Retrieve relevant chunks
        relevant_chunks = retrieve(payload.message, index, chunks, k=4)
        
        # Generate answer
        answer = generate_answer(payload.message, relevant_chunks)
        
        return ChatResponse(
            answer=answer,
            sources=relevant_chunks
        )
        
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Error generating answer: {str(e)}"
        )

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)