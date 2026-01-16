# rag_answer.py

from typing import List

def retrieve(query: str, index, chunks: List[str], k: int = 4) -> List[str]:
    """
    Fake retrieval for local testing. Returns top k chunks from the index.
    """
    # For demo, just return first k chunks
    return chunks[:k]

def generate_answer(user_question: str, retrieved_chunks: List[str]) -> str:
    """
    Fake answer generation for local testing.
    Just returns the first chunk as the answer.
    """
    if not retrieved_chunks:
        return "No matching info found in the documents."
    return retrieved_chunks[0]
