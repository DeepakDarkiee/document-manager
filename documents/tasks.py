import random

import ocrmypdf
from celery import Celery, shared_task
from celery.schedules import crontab

from documents.models import Document
from documents.utils import check_pdf

app = Celery()


@shared_task(name="converion")
def ocr_convert(output, filename, id):
    doc = Document.objects.get(id=id)
    input = doc.document.path
    file_name = doc.document.name
    read_content = check_pdf(input)
    # doc = Document.objects.filter(id=id)
    if read_content == None:
        ocrmypdf.ocr(input, output, deskew=True)
        doc.document = f"/ocr/{filename}.pdf"
        read_content = check_pdf(f"./media/ocr/{filename}.pdf")
        doc.content = read_content
    else:
        doc.content=read_content 
    doc.save()
    return True
