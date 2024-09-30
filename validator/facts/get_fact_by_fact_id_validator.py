import allure


@allure.step
def validate_fact_id(response, expected_fact_id):
    assert response.data.id == expected_fact_id, \
        f"Amount of facts: {response.data.id} != {expected_fact_id}"
