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



**Testcases:**
```markdown
|--------------|-----------------------------------------|----------------------------------------------------|------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------|
| Test Case ID | Test Title                              | Description                                        | Steps                                                                                                | Expected Result                                                         |
|--------------|-----------------------------------------|----------------------------------------------------|------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------|
| TC1          | Test Get Fact by Fact ID                | Tests getting a fact by its ID                     | - Send a GET request to `/facts/random` with `amount=10` to get 10 random facts.                     | The response has a status code of 200 and contains the correct fact ID. |                                        
|              |                                         |                                                    | - Pick one fact at random and get its ID.                                                            |                                                                         | 
|              |                                         |                                                    | - Send a GET request to `/facts/{factID}`.                                                           |                                                                         |
|              |                                         |                                                    | - Verify the status code.                                                                            |                                                                         |
|              |                                         |                                                    | - Verify that the fact ID in the response matches the selected fact ID.                              |                                                                         |
|--------------|-----------------------------------------|----------------------------------------------------|------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------|
| TC2          | Test Get Random Fact                    | Tests getting a random animal fact without params  | - Send a GET request to `/facts/random` without any parameters.                                      | Status code 200, animal type is `cat` (default), and the amount         |
|              |                                         |                                                    | - Validate the status code.                                                                          | is `1` (default).                                                       |
|              |                                         |                                                    | - Validate the animal type and the number of facts returned.                                         |                                                                         |
|--------------|-----------------------------------------|----------------------------------------------------|------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------|
| TC3          | Test Get Random Fact                    | Tests getting a random animal fact with animal type| - Send a GET request to `/facts/random` with `animal_type=dog`.                                      | Status code 200, animal type is `dog`, and the amount is `1` (default). |
|              |                                         |                                                    | - Validate the status code.                                                                          |                                                                         | 
|              |                                         |                                                    | - Validate the returned animal type and the amount.                                                  |                                                                         | 
|--------------|-----------------------------------------|----------------------------------------------------|------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------|
| TC4          | Test Get Random Fact                    | Tests getting multiple random animal facts by      | - Send a GET request to `/facts/random` with `amount=5`.                                             | Status code 200, animal type is `cat` (default), and the amount is `5`. |
|              |                                         | specifying an amount                               | - Validate the status code.                                                                          |                                                                         |
|              |                                         |                                                    | - Validate the animal type and the number of facts returned.                                         |                                                                         |
|--------------|-----------------------------------------|----------------------------------------------------|------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------|
| TC5          | Test Get Random Fact                    | Tests getting multiple random animal facts by      | - Send a GET request to `/facts/random` with `animal_type=dog` and `amount=5`.                       | Status code 200, animal type is `dog`, and the amount is `5`.           |
|              |                                         | specifying an animal type and amount               | - Validate the status code.                                                                          |                                                                         |
|              |                                         |                                                    | - Validate the animal type and the number of facts returned.                                         |                                                                         |
|--------------|-----------------------------------------|----------------------------------------------------|------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------|                                   
```



