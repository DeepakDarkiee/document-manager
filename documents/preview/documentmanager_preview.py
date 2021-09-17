from bridger import buttons as bt
from bridger import display as dp
from bridger.preview.metadata_config import PreviewConfig


class DocumentManagerPreviewConfig(PreviewConfig):
    def get_buttons(self):
        return [
            bt.HyperlinkButton(endpoint="https://www.google.com", label="Open Google"),
            bt.HyperlinkButton(
                endpoint="https://www.nytimes.com", label="Open NYTimes"
            ),
            bt.WidgetButton(key="self_endpoint", icon="wb-icon-data"),
        ]

    def get_display(self):
        return dp.InstanceDisplay(
            sections=tuple(
                [dp.Section(fields=dp.FieldSet(fields=tuple(["name", "status"])))]
            )
        )
