import allure

from utils.enumeration.status_code import StatusCodeEnum


@allure.step
def validate_status_code_success(actual_response):
    assert actual_response.status_code == StatusCodeEnum.SUCCESS, (
        f"status code {actual_response.status_code} different than {StatusCodeEnum.SUCCESS.value}")
