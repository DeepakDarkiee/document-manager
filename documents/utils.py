import ocrmypdf
import pdfplumber


def open_pdf(filename):
    pdf = pdfplumber.open(filename)
    page = pdf.pages[0]
    text = page.extract_text()

    return text


def convert(input,output):
    ocrmypdf.ocr(input,output,deskew=True)
    return True
    