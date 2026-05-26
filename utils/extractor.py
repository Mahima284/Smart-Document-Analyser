from pdfminer.high_level import extract_text as pdf_extract
from docx import Document

def extract_text(filepath):

    if filepath.endswith(".pdf"):

        return pdf_extract(filepath)

    elif filepath.endswith(".docx"):

        doc = Document(filepath)

        full_text = []

        for para in doc.paragraphs:
            full_text.append(para.text)

        return "\n".join(full_text)

    return "Unsupported file format"