# from bridger import buttons as bt
# from bridger.signals.instance_buttons import (
#     add_additional_resource,
#     add_instance_button,
# )
# from django.dispatch import receiver

# from todos.serializers import ToDoSerializer
# from todos.views import ToDoViewSet


# @receiver(add_instance_button, sender=ToDoViewSet)
# def test_adding_instance_buttons_ep(sender, many, *args, **kwargs):
#     return bt.HyperlinkButton(
#         icon="Open API",
#         label="",
#         endpoint="http://127.0.0.1:8000/todo/",
#         weight=1,
#     )
