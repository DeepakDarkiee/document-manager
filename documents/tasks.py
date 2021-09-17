import random

import ocrmypdf
from celery import Celery, shared_task
from celery.schedules import crontab

from documents.models import Document,Profile,Company
from documents.utils import check_pdf
from django.core.exceptions import ObjectDoesNotExist

app = Celery()


@shared_task(name="converion")
def ocr_convert(output, filename, id,user_id):
    try:
        user=Profile.objects.get(id=user_id)
    except ObjectDoesNotExist:
        pass
    try:
        user=Company.objects.get(id=user_id)
    except ObjectDoesNotExist:
        pass
    doc = Document.objects.get(id=id)
    user.document_manager.create(documents=doc)
    # doc=user.document_manager.documents.get(id=id)
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
