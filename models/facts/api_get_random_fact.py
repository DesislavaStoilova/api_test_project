import requests

from models.base_api import BaseApi
from models.facts.api_get_random_fact_response import ApiGetRandomFactResponse


class ApiGetRandomFact(BaseApi):

    def __init__(self):
        super().__init__()

    _api_path = "facts/random/"
    """
    API class getting random facts for passed animal
    """

    def get(self, animal_type: str = None, amount: int = None) -> ApiGetRandomFactResponse:
        params = {
            "animal_type": animal_type,
            "amount": amount
        }

        # send params with provided values, do not send None values
        params = {k: v for k, v in params.items() if v is not None}
        url = self.get_url(self._api_path)
        res = requests.get(url, params=params)

        try:
            if res.status_code == 200:
                self.logger.info(f"Successfully fetched random facts")
                return ApiGetRandomFactResponse(
                    status_code=res.status_code, data=res.json())

        except Exception as e:

            self.logger.error(f"An error occurred while fetching the random facts fact {e}")
            return ApiGetRandomFactResponse(
                status_code=res.status_code, data={"error": "An error occurred while fetching the random facts fact"})
