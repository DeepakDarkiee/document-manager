from django.contrib import admin

# Register your models here.
from documents.models import DocumentType, Document,DocumentManager,Profile,Company

admin.site.register(DocumentType)
admin.site.register(Document)
admin.site.register(DocumentManager)
admin.site.register(Profile)
admin.site.register(Company)