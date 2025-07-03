import allure


@allure.step
def validate_animal_type(response, expected_type=None):
    animal_types = response.data if isinstance(response.data, list) else [response.data]
    for animal_type in animal_types:
        if expected_type is not None:
            assert animal_type.type == expected_type, \
                f"Animal type: {animal_type.type} != {expected_type}"
        else:
            assert animal_type.type == "cat", \
                f"Animal type: {animal_type.type} != cat"


@allure.step
def validate_amount(response, expected_amount=None):
    if expected_amount is not None:
        assert len(response.data) == expected_amount, \
            f"Amount of facts: {len(response.data)} != {expected_amount}"
    else:
        # For default case, response.data should be a single fact (not a list)
        # If it's a list, it should have length 1; if it's a single object, we expect 1 fact
        if isinstance(response.data, list):
            assert len(response.data) == 1, \
                f"Amount of facts: {len(response.data)} != 1"
        else:
            # Single fact object means amount is 1
            assert True, "Single fact object detected, amount is 1"
