import fitz  # PyMuPDF

# Open the mock document we just generated
pdf = fitz.open("uploaded_pdfs/sample_handbook.pdf")

print(f"Total Pages Found: {len(pdf)}\n")

# Loop through and extract the textual layout blocks
for page_num, page in enumerate(pdf, 1):
    print(f"=== Page {page_num} Block Contents ===")
    text = page.get_text("blocks")
    for block in text:
        block_text = block[4].strip()  # Item index 4 contains the raw text string
        if block_text:
            print(block_text)
            print("-" * 20)