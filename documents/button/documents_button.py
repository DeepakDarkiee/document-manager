from bridger import buttons as bt
from bridger import display as dp
from bridger.buttons.metadata_config import ButtonConfig
# from documents.serializers import ActionButtonSerializer


class DocumentButtonConfig(ButtonConfig):
    # FSM_DROPDOWN = True
    CUSTOM_INSTANCE_BUTTONS = CUSTOM_LIST_INSTANCE_BUTTONS = {
        # bt.ActionButton(
        #     label="TestButton",
        #     icon="Mark Complete",
        #     key="markdone",
        #     instance_display=dp.InstanceDisplay(
        #         sections=(dp.Section(fields=dp.FieldSet(fields=("status",))),)
        #     ),
        #     serializer=ActionButtonSerializer,
        # )
          bt.HyperlinkButton(icon="mark-done", label="Mark Done",
        key="markdone")
    }
