import io
import json
import os
from subprocess import Popen

import ocrmypdf
from bridger.filters import FilterSet
from bridger.viewsets import ModelViewSet, RepresentationViewSet
from django.conf import settings
from rest_framework.decorators import action
from rest_framework.response import Response

from documents.models import Document, DocumentType
from documents.serializers import (DocumentSerializer,
                                   DocumentTypeRepresentationSerializer,
                                   DocumentTypeSerializer)

from .button.documents_button import DocumentButtonConfig
from .display.documents_display import DocumentDisplayConfig
from .display.type_display import DocumentTypeDisplayConfig
from .preview.documents_preview import DocumentPreviewConfig
from .titles.documents_title import DocumentTitleConfig
from .titles.type_title import TypeTitleConfig


class DocumentFilterSet(FilterSet):
    class Meta:
        model = Document
        fields = {"name": ["icontains"]}


class DocumentTypeRepresentationViewSet(RepresentationViewSet):
    queryset = DocumentType.objects.all()
    serializer_class = DocumentTypeRepresentationSerializer
import time

class DocumentTypeViewSet(ModelViewSet):
    display_config_class = DocumentTypeDisplayConfig
    title_config_class = TypeTitleConfig
    # preview_config_class = ToDoPreviewConfig
    # button_config_class = ToDoButtonConfig
    queryset = DocumentType.objects.all()
    serializer_class = DocumentTypeSerializer


class DocumentViewSet(ModelViewSet):
    """
    A viewset for viewing and editing user instances.
    """

    LIST_DOCUMENTATION = "/todos/documentation/to_do.md"
    display_config_class = DocumentDisplayConfig
    title_config_class = DocumentTitleConfig
    preview_config_class = DocumentPreviewConfig
    button_config_class = DocumentButtonConfig

    queryset = Document.objects.all()
    serializer_class = DocumentSerializer
    filterset_class = DocumentFilterSet
    search_fields = ["name", "content"]
    ordering_fields = ["name"]
    
    def create(self, request, *args, **kwargs):
        if request.data:
            print(request.data)
            document=request.data.get('document').file
            print(document)
            name=request.data.get('name')
            base_dir = settings.BASE_DIR
            output_file=os.path.join(base_dir ,f"media/ocr/{name}.pdf")
            ocrmypdf.ocr(document,output_file,deskew=True)
            # output_file=os.path.join(settings.MEDIA_ROOT ,f"media/ocr/{name}.pdf")
            # file_path = os.path.join(settings.MEDIA_ROOT,f"ocr/{name}.pdf",'w')
            # # file_path = settings.MEDIA_ROOT +'/ocr/'+ f"{name}.pdf"
            # file_path.close()
            # print(type(file_path))
            
            request.data.update({'document':f"./media/ocr/{name}.pdf"})
            # serializer = DocumentSerializer(data=request.data)
            # import pdb;pdb.set_trace()
            # if serializer.is_valid():
            #     uploaded=serializer.save()
                # process = Popen(['ocrmypdf', uploaded.document.path, f"./media/ocr/{name}.pdf"])
            return super(DocumentViewSet, self).create(request, *args, **kwargs)

    