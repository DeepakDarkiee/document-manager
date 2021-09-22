from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType
from django.db import models


class DocumentType(models.Model):
    type = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.type

    @classmethod
    def get_endpoint_basename(cls):
        return "type"

    @classmethod
    def get_endpoint(cls):
        return "type-list"

    def get_tag_detail_endpoint(self):
        return reverse("type-detail", args=[self.id])

    def get_tag_representation(self):
        return self.type

    @property
    def upper_char_field(self):
        return self.type.upper()

    @classmethod
    def get_representation_endpoint(cls):
        return "type-list"

    @classmethod
    def get_representation_value_key(cls):
        return "id"

    @classmethod
    def get_representation_label_key(cls):
        return "{{type}}"


class Document(models.Model):
    content = models.TextField(blank=True, null=True)
    name = models.CharField(max_length=255, blank=True)
    document = models.FileField(upload_to="documents/", null=True, blank=True)
    type = models.ForeignKey(
        DocumentType, on_delete=models.CASCADE, null=True, blank=True
    )
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    @classmethod
    def get_endpoint_basename(cls):
        return "document"

    @classmethod
    def get_endpoint(cls):
        return "document-list"

    def get_tag_detail_endpoint(self):
        return reverse("document-detail", args=[self.id])
 

    def get_tag_representation(self):
        return self.document

    @property
    def upper_char_field(self):
        return self.document.upper()

    @classmethod
    def get_representation_endpoint(cls):
        return "document-list"

    @classmethod
    def get_representation_value_key(cls):
        return "id"

    @classmethod
    def get_representation_label_key(cls):
        return "{{document}}"


class DocumentManager(models.Model):
    content_type = models.ForeignKey(
        ContentType,
        on_delete=models.CASCADE,
    )
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey()
    documents = models.ForeignKey(
        Document,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="documents",
    )

    def __str__(self):
        return str(self.id)

    @classmethod
    def get_endpoint_basename(cls):
        return "document_manager"

    @classmethod
    def get_endpoint(cls):
        return "document_manager_list"

    def get_tag_detail_endpoint(self):
        return reverse("document_manager_detail", args=[self.id])
    
    def get_tag_representation(self):
        return self.documents

    @property
    def upper_char_field(self):
        return self.documents.upper()

    @classmethod
    def get_representation_endpoint(cls):
        return "document_manager-list"

    @classmethod
    def get_representation_value_key(cls):
        return "id"

    @classmethod
    def get_representation_label_key(cls):
        return "{{documents}}"


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    created_at = models.DateTimeField(auto_now=True)
    document_manager = GenericRelation(DocumentManager)
    company = models.ForeignKey('Company',on_delete=models.CASCADE, related_name="company_profile")

    def __str__(self):
        return self.user.username
    
    def __str__(self):
        return str(self.id)

    @classmethod
    def get_endpoint_basename(cls):
        return "profile"

    @classmethod
    def get_endpoint(cls):
        return "profile_list"

    def get_tag_detail_endpoint(self):
        return reverse("profile_detail", args=[self.id])
    
    def get_tag_representation(self):
        return self.user

    @property
    def upper_char_field(self):
        return self.user.upper()

    @classmethod
    def get_representation_endpoint(cls):
        return "profile-list"

    @classmethod
    def get_representation_value_key(cls):
        return "id"

    @classmethod
    def get_representation_label_key(cls):
        return "{{user}}"


class Company(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="company")
    created_at = models.DateTimeField(auto_now=True)
    document_manager = GenericRelation(DocumentManager)

    def __str__(self):
        return self.user.username
