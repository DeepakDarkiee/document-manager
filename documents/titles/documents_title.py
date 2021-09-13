from bridger.titles.metadata_config import TitleConfig


class DocumentTitleConfig(TitleConfig):
    def get_instance_title(self):
        return "{{name}}"
