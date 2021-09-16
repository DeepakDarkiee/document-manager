import io
import os

import ocrmypdf
from bridger.filters import FilterSet
from bridger.viewsets import ModelViewSet, RepresentationViewSet
from django.conf import settings
from rest_framework.decorators import action
from rest_framework.response import Response

from documents.models import Document, DocumentType
from documents.serializers import (
    DocumentSerializer,
    DocumentTypeRepresentationSerializer,
    DocumentTypeSerializer,
)
from documents.tasks import ocr_convert

from .button.documents_button import DocumentButtonConfig
from .display.documents_display import DocumentDisplayConfig
from .display.type_display import DocumentTypeDisplayConfig
from .preview.documents_preview import DocumentPreviewConfig
from .titles.documents_title import DocumentTitleConfig
from .titles.type_title import TypeTitleConfig


class DocumentFilterSet(FilterSet):
    class Meta:
        model = Document
        fields = {"name": ["icontains"], "content": ["icontains"]}


class DocumentTypeRepresentationViewSet(RepresentationViewSet):
    queryset = DocumentType.objects.all()
    serializer_class = DocumentTypeRepresentationSerializer


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

    # def create(self, request, *args, **kwargs):
    #     if request.data:
    #         serializer = DocumentSerializer(data=request.data)
    #         if serializer.is_valid():
    #             uploaded = self.perform_create(serializer)
    #             data_id = uploaded.id
    #         name = request.data.get("name")
    #         base_dir = settings.BASE_DIR
    #         output_file = os.path.join(base_dir, f"media/ocr/{name}.pdf")
    #         print(type(output_file))
    #         ocr_convert.delay(output_file, name, data_id)
    #         request.data["id"] = data_id
    #         print(request.data)
    #         return Response(serializer.data, status=201)

    def perform_create(self, serializer):
        # serializer = DocumentSerializer(data=request.data)
        if serializer.is_valid():
            uploaded = serializer.save()
            data_id = uploaded.id
        name = uploaded.name
        base_dir = settings.BASE_DIR
        output_file = os.path.join(base_dir, f"media/ocr/{name}.pdf")
        print(type(output_file))
        ocr_convert.delay(output_file, name, data_id)
        return uploaded
