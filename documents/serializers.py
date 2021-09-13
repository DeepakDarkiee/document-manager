from bridger import serializers
from bridger.serializers import (
    CharField,
    IntegerField,
    Serializer,
    TextField,
    register_resource,
)
from rest_framework.reverse import reverse

from documents.models import Document, DocumentType

# class ActionButtonSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = ToDo
#         fields = ["id", "status"]


class DocumentTypeRepresentationSerializer(serializers.RepresentationSerializer):

    _detail = serializers.HyperlinkField(reverse_name="type-detail")

    class Meta:
        model = DocumentType
        fields = ("id", "type", "_detail")


class DocumentTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = DocumentType
        fields = ["id", "type", "_additional_resources"]


class DocumentSerializer(serializers.ModelSerializer):
    _type = DocumentTypeRepresentationSerializer(source="document_type")

    class Meta:
        model = Document
        fields = [
            "id",
            "name",
            "content",
            "document",
            "_type",
            "type",
            "uploaded_at",
            "_additional_resources",
        ]

    # @register_resource()
    # def markdone(self, instance, request, user):
    #     return {"markdone": reverse("todo-markdone", args=[instance.id])}


# .../serializers.py


# class CustomShareSerializer(Serializer):
#     user_id = IntegerField(label="User ID")
#     widget_endpoint = CharField(label="Widget URL")
#     message = TextField(label="Message", default="Check out this Widget.")

#     some_additional_field = IntegerField(label="Some Additional Field")
