import allure
import pytest

from models.facts.api_get_random_fact import ApiGetRandomFact
from validator.common_validator import validate_status_code_success
from validator.facts.get_random_fact_validator import validate_animal_type, validate_amount


@pytest.mark.TestGetRandomFact
@allure.title("Test Get Random Fact")
@allure.description("Tests for getting random animal fact"
                    "Optional parameters: "
                    "animal_type - default value: cat"
                    "amount - default value: 1")
@pytest.mark.normal
class TestGetRandomFact:
    api_get_random_fact = ApiGetRandomFact()

    @allure.description("Send a get request to /facts/random without passing parameters"
                        "Expected result: get random fact with the default parameters")
    def test_get_random_without_passing_parameters(self):
        res = self.api_get_random_fact.get()
        validate_status_code_success(res)
        validate_animal_type(response=res)
        validate_amount(response=res)

    @allure.description("Send a get request to /facts/random with passing parameter: animal_type"
                        "Expected result: get random fact for passed animal_type and the default amount")
    def test_get_random_with_passing_animal_type(self):
        animal_type = "dog"
        res = self.api_get_random_fact.get(animal_type=animal_type)
        validate_status_code_success(res)
        validate_animal_type(response=res, expected_type=animal_type)
        validate_amount(response=res)

    @allure.description("Send a get request to /facts/random with passing parameter: amount"
                        "Expected result: get random fact for the default animal_type and passed amount")
    def test_get_random_with_passing_amount(self):
        amount = 5
        res = self.api_get_random_fact.get(amount=amount)
        validate_status_code_success(res)
        validate_animal_type(response=res)
        validate_amount(response=res, expected_amount=amount)

    @allure.description("Send a get request to /facts/random with passing parameter: amount"
                        "Expected result: get random fact for the passed animal_type and passed amount")
    def test_get_random_with_passing_animal_type_and_amount(self):
        animal_type = "dog"
        amount = 5
        res = self.api_get_random_fact.get(animal_type=animal_type, amount=amount)
        validate_status_code_success(res)
        validate_animal_type(response=res, expected_type=animal_type)
        validate_amount(response=res, expected_amount=amount)
