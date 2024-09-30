import random

import allure
import pytest

from models.facts.api_get_fact_by_fact_id import ApiGetFactByFactID
from models.facts.api_get_random_fact import ApiGetRandomFact
from validator.common_validator import validate_status_code_success
from validator.facts.get_fact_by_fact_id_validator import validate_fact_id


@pytest.mark.TestGetFactByFactID
@allure.title("Test Get Fact by fact ID")
@allure.description("Tests for getting fact by passing the fact ID"
                    "Steps:"
                    "1. Send a get request to /facts/random with amount 10 to get 10 random facts"
                    "2. Pick one fact with random choice and get the fact id"
                    "3. Send a get request to /facts/{factID}"
                    "4. Verify the status code"
                    "5. Verify that the fact id in the /facts/{factID}"
                    "response is the same as the selected one in step 2")
@pytest.mark.normal
class TestGetFactByFactID:
    api_get_random_fact = ApiGetRandomFact()
    api_get_fact_by_fact_id = ApiGetFactByFactID()

    def test_fact_by_fact_id(self):
        random_fact_response = self.api_get_random_fact.get(amount=10)
        select_fact = random.choice(random_fact_response.data)
        fact_by_fact_id_response = self.api_get_fact_by_fact_id.get(fact_id=select_fact.id)
        validate_status_code_success(actual_response=fact_by_fact_id_response)
        validate_fact_id(fact_by_fact_id_response, select_fact.id)



