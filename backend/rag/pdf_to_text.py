from pypdf import PdfReader
import os

def pdf_to_text(pdf_path: str) -> str:
    """
    Extract text from a PDF file and clean it.
    
    Args:
        pdf_path: Path to the PDF file
        
    Returns:
        Cleaned text content from the PDF
    """
    if not os.path.exists(pdf_path):
        raise FileNotFoundError(f"PDF not found at: {pdf_path}")
    
    reader = PdfReader(pdf_path)
    pages = []
    
    for page in reader.pages:
        text = page.extract_text()
        if text:
            pages.append(text)
    
    # Join all pages
    full_text = "\n".join(pages)
    
    # Clean up the text
    full_text = full_text.replace("\r", "\n")
    lines = [line.strip() for line in full_text.split("\n") if line.strip()]
    clean_text = "\n".join(lines)
    
    return clean_text

if __name__ == "__main__":
    # Test the extraction
    test_path = "backend/data/knowledge.pdf"
    if os.path.exists(test_path):
        text = pdf_to_text(test_path)
        print(f"Extracted {len(text)} characters")
        print("\nFirst 500 characters:")
        print(text[:500])
    else:
        print(f"Please create sample PDF first by running make_sample_pdf.py")