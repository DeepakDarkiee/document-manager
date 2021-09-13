from bridger.buttons import WidgetButton
from bridger.notifications.models import Notification


def share_notification(user_id, widget_endpoint, message, some_additional_field, user):
    # Make sure that all the fields that are used in the Serializer are present as parameters and the user
    _, endpoint = widget_endpoint.split("?widget_endpoint=")
    Notification.objects.create(
        recipient_id=user_id,
        title=f"{user.first_name} {user.last_name} shared a widget with you",
        message=message,
        buttons=[
            dict(WidgetButton(label="Open", icon="wb-icon-data", endpoint=endpoint))
        ],
    )
