import pdfplumber


def check_pdf(filename):
    pdf = pdfplumber.open(filename)
    page = pdf.pages[0]
    text = page.extract_text()
    return text


    