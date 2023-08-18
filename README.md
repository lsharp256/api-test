# API-test
This repository contains automated API tests for https://v6.exchangerate-api.com/v6/1fc80820c72b0163bc9c7536/latest/USD. The tests are written in Python and use pytest.
 
---

## Getting Started
---
These instructions will provide guidance on setting up the test suite on your local machine.

## Prerequisites
- Python 3.9 or higher
- pytest
- virtual environment (https://virtualenv.pypa.io/en/stable/installation.html)

## Installation
1. Navigate to the project directory after cloning the repo:
    > `cd api-test`
2. Install the required dependencies:
    > `pip install -r requirements.txt`

## Running the tests
Run all tests with the following command:
> `pytest`

Run a specific test with:
> `pytest path/to/test.py::test_name`

## Test Scenarios

The test suite includes various scenarios. Here are the areas that were covered:
- Verifying that the endpoint returns a 200 status
- Verifying the total number of currencies returned
- Verifying the currency 'GBP' is shown within the response