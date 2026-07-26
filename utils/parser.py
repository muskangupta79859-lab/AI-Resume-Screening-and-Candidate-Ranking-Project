import fitz  # PyMuPDF
import pdfplumber
from docx import Document

def extract_text_from_pdf(file):
    """Extract text from PDF using PyMuPDF with pdfplumber fallback."""
    text = ""

    try:
        pdf = fitz.open(stream=file.read(), filetype="pdf")

        for page in pdf:
            text += page.get_text()

        pdf.close()

    except Exception:
        file.seek(0)

        with pdfplumber.open(file) as pdf:
            for page in pdf.pages:
                page_text = page.extract_text()

                if page_text:
                    text += page_text

    return text


def extract_text_from_docx(file):
    """Extract text from DOCX."""
    doc = Document(file)

    text = ""

    for para in doc.paragraphs:
        text += para.text + "\n"

    return text


def extract_resume_text(uploaded_file):
    """Detect file type and extract text."""

    if uploaded_file.name.endswith(".pdf"):
        return extract_text_from_pdf(uploaded_file)

    elif uploaded_file.name.endswith(".docx"):
        return extract_text_from_docx(uploaded_file)

    else:
        return ""