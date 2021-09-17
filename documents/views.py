import io
import os
from django.core.exceptions import ObjectDoesNotExist
import ocrmypdf
from bridger.filters import FilterSet
from bridger.viewsets import ModelViewSet, RepresentationViewSet
from django.conf import settings
from rest_framework.decorators import action
from rest_framework.response import Response
from django.contrib.auth.models import User
from documents.models import Document, DocumentType,DocumentManager, Profile
from documents.serializers import (
    DocumentRepresentationSerializer,
    DocumentSerializer,
    DocumentTypeRepresentationSerializer,
    DocumentTypeSerializer,
    DocumentManagerSerializer,
    ProfileSerializer,
)
from documents.tasks import ocr_convert

from .button.documents_button import DocumentButtonConfig
from .button.documentmanager_button import DocumentManagerButtonConfig
from .display.documents_display import DocumentDisplayConfig
from .display.type_display import DocumentTypeDisplayConfig
from .display.documentmanager_display import DocumentManagerDisplayConfig
from .display.profile_display import ProfileDisplayConfig
from .preview.documents_preview import DocumentPreviewConfig
from .preview.documentmanager_preview import DocumentManagerPreviewConfig
from .titles.documents_title import DocumentTitleConfig
from .titles.type_title import TypeTitleConfig
from .titles.documentmanager_title import DocumentManagerTitleConfig
from .titles.profile_title import ProfileTitleConfig


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

    def perform_create(self,serializer):
        # serializer = DocumentSerializer(data=request.data)
        if serializer.is_valid():
            uploaded = serializer.save()
            data_id = uploaded.id
            
        # user = self.request.user.profile
        try:
            user = self.request.user.profile
        except ObjectDoesNotExist:
            pass
        try:
            user = self.request.user.company
        except ObjectDoesNotExist:
            pass
        name = uploaded.name
        base_dir = settings.BASE_DIR
        output_file = os.path.join(base_dir, f"media/ocr/{name}.pdf")
        print(type(output_file))
        ocr_convert.delay(output_file, name, data_id,user.id)
        return uploaded


class DocumentManagerViewSet(ModelViewSet):
    """
    A viewset for viewing and editing user instances.
    """

    LIST_DOCUMENTATION = "/todos/documentation/to_do.md"
    display_config_class = DocumentManagerDisplayConfig
    title_config_class = DocumentManagerTitleConfig
    # preview_config_class = DocumentManagerPreviewConfig
    # button_config_class = DocumentManagerButtonConfig

    queryset = DocumentManager.objects.all()
    serializer_class = DocumentManagerSerializer
    # filterset_class = DocumentFilterSet
    # search_fields = ["name", "content"]
    # ordering_fields = ["name"]
    
    
class ProfileViewSet(ModelViewSet):
    """
    A viewset for viewing and editing user instances.
    """

    display_config_class = ProfileDisplayConfig
    title_config_class = ProfileTitleConfig
    # preview_config_class = DocumentManagerPreviewConfig
    # button_config_class = DocumentManagerButtonConfig

    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer