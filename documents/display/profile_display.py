from typing import Optional

from bridger import display as dp
from bridger.display.metadata_config import DisplayConfig


class ProfileDisplayConfig(DisplayConfig):
    # def get_instance_display(self) -> Optional[dp.InstanceDisplay]:
    #     return dp.InstanceDisplay(
    #         sections=(dp.Section(fields=dp.FieldSet(fields=("user", "created_at",))),)
    #     )

    def get_list_display(self) -> Optional[dp.ListDisplay]:
        return dp.ListDisplay(
            fields=[
                dp.Field(key="user", label="User"),
                dp.Field(key="created_at", label="created_at"),
            ],
        )
