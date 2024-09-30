import requests

from models.base_api import BaseApi
from models.facts.api_get_fact_by_fact_id_response import ApiGetFactByFactIDResponse


class ApiGetFactByFactID(BaseApi):

    def __init__(self):
        super().__init__()

    _api_path = "facts/{fact_id}"
    """
    API class getting facts by passed path parameter: fact ID
    """

    def get(self, fact_id: str = None) -> ApiGetFactByFactIDResponse:

        api_path = self._api_path.format(fact_id=fact_id)
        url = self.get_url(api_path)
        res = requests.get(url)

        try:
            if res.status_code == 200:
                self.logger.info(f"Successfully fetched fact with ID {fact_id}")
                return ApiGetFactByFactIDResponse(
                    status_code=res.status_code, data=res.json())

        except Exception as e:

            self.logger.error(f"An error occurred while fetching the fact {e}")
            return ApiGetFactByFactIDResponse(
                status_code=res.status_code, data={"error": "An error occurred while fetching the fact"})
