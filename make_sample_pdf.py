import os
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle

def generate_mock_pdf():
    # Set path inside your uploaded_pdfs folder
    pdf_path = os.path.join("uploaded_pdfs", "sample_handbook.pdf")
    os.makedirs("uploaded_pdfs", exist_ok=True)

    doc = SimpleDocTemplate(pdf_path, pagesize=letter, rightMargin=72, leftMargin=72, topMargin=72, bottomMargin=72)
    story = []

    styles = getSampleStyleSheet()
    title_style = ParagraphStyle('TitleStyle', parent=styles['Heading1'], fontSize=24, spaceAfter=20)
    body_style = ParagraphStyle('BodyStyle', parent=styles['Normal'], fontSize=11, leading=16, spaceAfter=12)

    # Title
    story.append(Paragraph("Acme Corp Employee Handbook", title_style))
    story.append(Spacer(1, 12))

    # Section 1
    story.append(Paragraph("<b>Section 1: Paid Time Off (PTO) Policy</b>", styles['Heading2']))
    story.append(Paragraph(
        "All full-time employees at Acme Corp receive 15 days of paid time off (PTO) annually. "
        "This time is accrued monthly at a rate of 1.25 days per month worked. "
        "Employees must request time off at least two weeks in advance through the company HR portal.",
        body_style
    ))
    story.append(Spacer(1, 12))

    # Section 2
    story.append(Paragraph("<b>Section 2: Sick Leave & Wellness</b>", styles['Heading2']))
    story.append(Paragraph(
        "Employees receive 10 sick days annually to care for their personal health or the health of immediate family members. "
        "Unused sick leave does not roll over into the next calendar year and cannot be cashed out upon separation.",
        body_style
    ))

    doc.build(story)
    print(f"Success! Mock PDF created at: {pdf_path}")

if __name__ == "__main__":
    generate_mock_pdf()