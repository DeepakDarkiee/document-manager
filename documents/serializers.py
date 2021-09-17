from bridger import serializers
from bridger.serializers import (
    CharField,
    IntegerField,
    Serializer,
    TextField,
    register_resource,
)
from rest_framework.reverse import reverse
from django.contrib.auth.models import User
from documents.models import Document, DocumentType,DocumentManager,Profile
from generic_relations.relations import GenericRelatedField
# class ActionButtonSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = ToDo
#         fields = ["id", "status"]


class DocumentTypeRepresentationSerializer(serializers.RepresentationSerializer):

    _detail = serializers.HyperlinkField(reverse_name="type-detail")

    class Meta:
        model = DocumentType
        fields = ("id", "type", "_detail")

class DocumentRepresentationSerializer(serializers.RepresentationSerializer):

    _detail = serializers.HyperlinkField(reverse_name="document-detail")

    class Meta:
        model = Document
        fields = ("id",  "document", "_detail",)
        
class DocumentManagerRepresentationSerializer(serializers.RepresentationSerializer):

    _detail = serializers.HyperlinkField(reverse_name="document_manager-detail")

    class Meta:
        model = DocumentManager
        fields = ("id",  "documents", "_detail",)
        
# class UserRepresentationSerializer(serializers.RepresentationSerializer):

#     _detail = serializers.HyperlinkField(reverse_name="user-detail")

#     class Meta:
#         model = User
#         fields = ("id",  "username", "_detail",)
        

class DocumentTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = DocumentType
        fields = ["id", "type", "_additional_resources"]
        
# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ["id", "username", "_additional_resources"]



class DocumentSerializer(serializers.ModelSerializer):
    _type = DocumentTypeRepresentationSerializer(source="type")

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


class DocumentManagerSerializer(serializers.ModelSerializer):
    _documents = DocumentRepresentationSerializer(source="documents")
    
        
    class Meta:
        model = DocumentManager
        fields = [
            "id",
            "content_type",
            "object_id",
            "content_object",
            "documents",
            "_documents",
            "_additional_resources",
        ]


class ProfileSerializer(serializers.ModelSerializer):
    document_manager = GenericRelatedField({DocumentManager: serializers.HyperlinkField(reverse_name="document-detail")})

    class Meta:
        model = Profile
        fields = [
            "id",
            "user",
            "created_at",
            "document_manager",
            "_additional_resources",
        ]
