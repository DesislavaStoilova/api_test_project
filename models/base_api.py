from utils.config.configuration import Configuration
from utils.logger import Logger


class BaseApi:
    def __init__(self):
        self.url = None
        self.logger = Logger()

    def get_url(self, path=None):
        self.url = Configuration().get_cat_facts_base_url() + path

        return self.url
