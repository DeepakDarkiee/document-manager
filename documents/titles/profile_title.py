from bridger.titles.metadata_config import TitleConfig


class ProfileTitleConfig(TitleConfig):
    def get_instance_title(self):
        return "{{user}}"
