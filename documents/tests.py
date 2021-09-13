# from django.test import Client, TestCase
# from django.urls import reverse
# from rest_framework import status
# from rest_framework.test import APIClient

# from todos.models import Category, ToDo


# class ToDoTestCase(TestCase):
#     def setUp(self):

#         self.client = APIClient()

#     def test_01_api_can_get_a_todo_instance(self):

#         todo = ToDo.objects.create(name="todo1")
#         response = self.client.get(reverse("todo-list"), args=(todo.pk,))
#         self.assertEqual(response.status_code, status.HTTP_200_OK)

#     def test_02_api_can_get_a_todo_list(self):

#         response = self.client.get(reverse("todo-list"))
#         self.assertEqual(response.status_code, status.HTTP_200_OK)


# class CategoryTestCase(TestCase):
#     def setUp(self):

#         self.client = APIClient()

#     def test_01_api_can_get_a_category_instance(self):

#         category = Category.objects.create(name="category1")
#         response = self.client.get(reverse("category-list"), args=(category.pk,))
#         self.assertEqual(response.status_code, status.HTTP_200_OK)

#     def test_02_api_can_get_a_category_list(self):

#         response = self.client.get(reverse("category-list"))
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
