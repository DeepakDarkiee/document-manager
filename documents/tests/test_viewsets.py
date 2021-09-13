# import pytest
# from django.test import Client, TestCase
# from django.urls import reverse
# from rest_framework import status
# from rest_framework.test import APIClient
# from todos.models import Category, ToDo
# from todos.views import CategoryRepresentationViewSet, CategoryViewSet, ToDoViewSet


# class TestToDoViewSet:
#     def test_as_view_list(self):
#         viewset = ToDoViewSet.as_view({"get": "list"})
#         assert viewset

#     def test_as_view_instance(self):
#         viewset = ToDoViewSet.as_view({"get": "retrieve"})
#         assert viewset

    


# class TestCategoryViewSet:
#     def test_as_view_list(self):
#         viewset = CategoryViewSet.as_view({"get": "list"})
#         assert viewset

#     def test_as_view_instance(self):
#         viewset = CategoryViewSet.as_view({"get": "retrieve"})
#         assert viewset

  


# class TestCategoryRepresentationViewSet:
#     def test_as_view_list(self):
#         viewset = CategoryRepresentationViewSet.as_view({"get": "list"})
#         assert viewset

#     def test_as_view_instance(self):
#         viewset = CategoryRepresentationViewSet.as_view({"get": "retrieve"})
#         assert viewset
