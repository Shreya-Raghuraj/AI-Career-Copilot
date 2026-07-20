import fitz


def extract_text_from_pdf(pdf_path):
    document = fitz.open(pdf_path)

    text = ""

    for page in document:
        text += page.get_text()

    document.close()

    # Clean text
    text = text.replace("\n", " ")
    text = " ".join(text.split())

    return text