import tiktoken
from typing import List

def chunk_text(
    text: str, 
    chunk_tokens: int = 450, 
    overlap_tokens: int = 80
) -> List[str]:
    """
    Split text into overlapping chunks based on token count.
    
    Args:
        text: The text to chunk
        chunk_tokens: Maximum tokens per chunk
        overlap_tokens: Number of tokens to overlap between chunks
        
    Returns:
        List of text chunks
    """
    # Use the same encoding as OpenAI's models
    enc = tiktoken.get_encoding("cl100k_base")
    
    # Encode the entire text
    tokens = enc.encode(text)
    
    chunks = []
    start = 0
    
    while start < len(tokens):
        # Define the end of this chunk
        end = start + chunk_tokens
        
        # Get the chunk and decode it
        chunk_tokens_slice = tokens[start:end]
        chunk = enc.decode(chunk_tokens_slice)
        chunks.append(chunk)
        
        # Move start forward, accounting for overlap
        start = end - overlap_tokens
        
        # Prevent negative start
        if start < 0:
            start = 0
            
        # If we've moved past the end, break
        if start >= len(tokens):
            break
    
    return chunks

if __name__ == "__main__":
    # Test chunking
    test_text = "This is a test sentence. " * 200
    chunks = chunk_text(test_text, chunk_tokens=100, overlap_tokens=20)
    print(f"Created {len(chunks)} chunks")
    print(f"\nFirst chunk ({len(chunks[0])} chars):")
    print(chunks[0][:200])