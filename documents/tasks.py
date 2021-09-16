import random

from celery import Celery, shared_task
from celery.schedules import crontab
from core.utils import convert, open_pdf

app = Celery()

@shared_task(name="converion")
def ocr_convert(input,output,myfile_name,id):
  from core.models import Document
  convert(input,output)
  doc = Document.objects.filter(id=id)
  text = open_pdf(f"./media/{myfile_name}_ocr.pdf")
  doc.update(document=f"./{myfile_name}_ocr.pdf", description=text)
  return True
