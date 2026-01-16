import json
import os
import numpy as np
import faiss
from openai import OpenAI
from typing import List, Tuple

# Get embedding model from environment or use default
EMBED_MODEL = os.getenv("EMBED_MODEL", "text-embedding-3-small")

# Initialize OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def embed_texts(texts: List[str]) -> np.ndarray:
    """
    Fake embeddings for local testing (no OpenAI call)
    """
    dim = 1536  # same as text-embedding-3-small
    vectors = np.random.rand(len(texts), dim).astype("float32")
    faiss.normalize_L2(vectors)
    return vectors


def build_and_save_index(
    chunks: List[str], 
    index_path: str, 
    meta_path: str
) -> None:
    """
    Build FAISS index from text chunks and save to disk.
    
    Args:
        chunks: List of text chunks
        index_path: Path to save FAISS index
        meta_path: Path to save chunk metadata
    """
    print(f"Embedding {len(chunks)} chunks...")
    vectors = embed_texts(chunks)
    
    # Get dimension of embeddings
    dim = vectors.shape[1]
    
    # Create FAISS index (inner product = cosine similarity with normalized vectors)
    index = faiss.IndexFlatIP(dim)
    index.add(vectors)
    
    print(f"Saving index with {index.ntotal} vectors...")
    
    # Save index
    faiss.write_index(index, index_path)
    
    # Save metadata (the actual text chunks)
    with open(meta_path, "w", encoding="utf-8") as f:
        json.dump({"chunks": chunks}, f, ensure_ascii=False, indent=2)
    
    print(f"Index saved to {index_path}")
    print(f"Metadata saved to {meta_path}")

def load_index(index_path: str, meta_path: str) -> Tuple[faiss.Index, List[str]]:
    """
    Load FAISS index and metadata from disk.
    
    Args:
        index_path: Path to FAISS index file
        meta_path: Path to metadata JSON file
        
    Returns:
        Tuple of (FAISS index, list of chunks)
    """
    if not os.path.exists(index_path):
        raise FileNotFoundError(f"Index not found at {index_path}")
    if not os.path.exists(meta_path):
        raise FileNotFoundError(f"Metadata not found at {meta_path}")
    
    # Load FAISS index
    index = faiss.read_index(index_path)
    
    # Load metadata
    with open(meta_path, "r", encoding="utf-8") as f:
        meta = json.load(f)
    
    chunks = meta["chunks"]
    
    print(f"Loaded index with {index.ntotal} vectors and {len(chunks)} chunks")
    
    return index, chunks