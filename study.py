from pypdf import PdfReader
import io

#extracting text from pdf
def extract_text_from_pdf(pdf_file):

    pdf_bytes = pdf_file.read()
    pdf_stream = io.BytesIO(pdf_bytes)

    reader = PdfReader(pdf_stream)

    text = ""
    for page in reader.pages:
        text += page.extract_text() + "\n"
    return text



