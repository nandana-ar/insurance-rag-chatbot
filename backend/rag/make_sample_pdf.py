from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import os

def make_pdf(path="data/knowledge.pdf"):
    # Ensure directory exists
    os.makedirs(os.path.dirname(path), exist_ok=True)
    
    c = canvas.Canvas(path, pagesize=letter)
    text = c.beginText(40, 750)
    text.setFont("Helvetica", 11)
    
    lines = [
        "Insurance Agency Customer Care Knowledge Base",
        "",
        "=" * 60,
        "",
        "Q: How do I file a claim?",
        "A: To file a claim, call our 24/7 claims line at 1-800-CLAIM-NOW or",
        "submit through our online portal at www.insurance.com/claims.",
        "Please keep all photos, receipts, and documentation related to the incident.",
        "A claims adjuster will contact you within 24-48 hours.",
        "",
        "Q: What is a deductible?",
        "A: A deductible is the amount you pay out of pocket before your insurance",
        "coverage begins to pay. For example, if you have a $500 deductible and",
        "a $3,000 claim, you pay $500 and insurance pays $2,500.",
        "",
        "Q: How do I add a driver to my auto policy?",
        "A: To add a driver, provide their full name, date of birth, driver's license",
        "number, and the effective date you want them added. We'll run a quick check",
        "and send you a quote for any premium change within 1 business day.",
        "",
        "Q: What documents do you need for a new policy?",
        "A: For a new policy, we need: valid photo ID, proof of address (utility bill",
        "or lease), vehicle registration or home details, and your prior insurance",
        "history if applicable. This helps us provide accurate quotes.",
        "",
        "Q: How do I cancel my policy?",
        "A: To cancel your policy, call us at 1-800-555-0123 or email",
        "support@insurance.com. Please provide at least 30 days notice to avoid",
        "cancellation fees. We'll process a pro-rated refund if applicable.",
        "",
        "Q: What is covered under comprehensive auto insurance?",
        "A: Comprehensive coverage protects against non-collision damage like theft,",
        "vandalism, fire, hail, flood, and animal strikes. It does NOT cover",
        "collision damage or liability - those require separate coverages.",
        "",
        "Q: How often should I review my insurance policy?",
        "A: We recommend reviewing your policy annually, or whenever you have a major",
        "life change such as marriage, buying a home, having children, or changing jobs.",
        "This ensures you have adequate coverage.",
        "",
        "Q: What is liability insurance?",
        "A: Liability insurance covers damage you cause to others. This includes bodily",
        "injury and property damage. Minimum required amounts vary by state, but we",
        "recommend higher limits for better protection.",
    ]
    
    for line in lines:
        text.textLine(line)
    
    c.drawText(text)
    c.showPage()
    c.save()
    print(f"Sample PDF created at: {path}")

if __name__ == "__main__":
    make_pdf()