# api_test_project

**Project Overview**

This project automates testing of API endpoints for https://cat-fact.herokuapp.com/#/. It uses requests module, pydantic module for field validation, pytest, and Allure for reporting. 



**Instalation steps:**

Clone the Repository
Create and activate a Virtual Environment
Run the following command to create a virtual environment
```bash
python -m venv venv
```
Run the following command activate it
```bash
source venv/bin/activate
```
Install Requirements
Install all required dependencies listed in the requirements.txt file:
```bash
pip install -r requirements.txt or pip3 install -r requirements.txt
```
Run the tests
To run tests using pytest and allure, use the following command:
```bash
pytest --alluredir=reports/allure-results
```
Open the generated report
To open the generated allure report run the following command:
```bash
allure serve reports/allure-results
```


**Project structure:**

```bash
├── config_sample/
│   └── config_sample.yaml
├── models/
│   ├── facts/
│   │   ├── api_get_fact_by_fact_id.py
│   │   ├── api_get_fact_by_fact_id_response.py
│   │   ├── api_get_random_fact.py
│   │   └── api_get_random_fact_response.py
│   └── users/
│       └── base_api.py
├── reports/
├── tests/
│   └── facts/
│       ├── test_get_fact_by_fact_id.py
│       └── test_get_random_fact.py
├── utils/
│   ├── config/
│   │   ├── config.yaml
│   │   └── configuration.py
│   ├── enumeration/
│   │   ├── status_code.py
│   │   └── logger.py
│   └── validator/
│       └── facts/
│           └── common_validator.py
├── pytest.ini
├── README.md
└── requirements.txt
```






