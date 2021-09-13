from typing import Optional

from bridger import display as dp
from bridger.display.metadata_config import DisplayConfig


class DocumentDisplayConfig(DisplayConfig):
    def get_instance_display(self) -> Optional[dp.InstanceDisplay]:
        return dp.InstanceDisplay(
            sections=(dp.Section(fields=dp.FieldSet(fields=("name", "type"))),)
        )

    def get_list_display(self) -> Optional[dp.ListDisplay]:
        return dp.ListDisplay(
            fields=[
                dp.Field(key="name", label="Name"),
                dp.Field(key="type", label="type"),
            ],
        )
