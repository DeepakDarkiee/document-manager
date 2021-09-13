from bridger.filters import FilterSet
from bridger.viewsets import ModelViewSet, RepresentationViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
import ocrmypdf
from documents.models import Document, DocumentType
from documents.serializers import (
    DocumentSerializer,
    DocumentTypeRepresentationSerializer,
    DocumentTypeSerializer,
)
import os

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
            document=request.data.get('document').file
            name=request.data.get('name')
            # import pdb;pdb.set_trace()
            output_name=str(document)
            ocrmypdf.ocr(document,os.path.join(f"./media/{name}.pdf"),
                    deskew=True,
                )
            return super(DocumentViewSet, self).create(request, *args, **kwargs)


    # @action(
    #     detail=True,
    #     methods=["GET", "POST"],
    # )
    # def markdone(self, request, pk):
    #     if request.method == "POST":
    #         status = request.POST.get("status")
    #         data = ToDo.objects.filter(pk=pk).update(status=status)

    #     return Response(data=data)
