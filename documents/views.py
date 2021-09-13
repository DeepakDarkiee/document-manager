from bridger.filters import FilterSet
from bridger.viewsets import ModelViewSet, RepresentationViewSet
from rest_framework.decorators import action
from rest_framework.response import Response

from documents.models import Document, DocumentType
from documents.serializers import (
    DocumentSerializer,
    DocumentTypeRepresentationSerializer,
    DocumentTypeSerializer,
)

from .button.documents_button import DocumentButtonConfig
from .display.documents_display import DocumentDisplayConfig
from .display.type_display import TypeDisplayConfig
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
    display_config_class = TypeDisplayConfig
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

    # @action(
    #     detail=True,
    #     methods=["GET", "POST"],
    # )
    # def markdone(self, request, pk):
    #     if request.method == "POST":
    #         status = request.POST.get("status")
    #         data = ToDo.objects.filter(pk=pk).update(status=status)

    #     return Response(data=data)
