from bridger.titles.metadata_config import TitleConfig


class TypeTitleConfig(TitleConfig):
    def get_instance_title(self):
        return "{{type}}"
