from bridger.titles.metadata_config import TitleConfig


class DocumentManagerTitleConfig(TitleConfig):
    def get_instance_title(self):
        return "{{name}}"
