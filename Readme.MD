README.md
#  Playwright E2E Test Suite: Employee Management Flow

This repository contains a small test suite built with Playwright and pytest to automate the employee management flow of a sample HR platform. 

Current Tests are:
- Add a new employee
- Edit employee details
- Delete employee and verify removal


---

## How to run this project

### 1. Clone the repository

```bash
git clone https://github.com/AngelBorja/paylocity-automation-challenge.git
cd paylocity-automation-challenge
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

Required packages:
- playwright
- pytest
- pytest-dependency
- python-dotenv

### 3. Install Playwright browsers
```bash
playwright install
```


### 4.Create Environment Variables
Create a .env file in the project root:
TEST_USERNAME="Add your usename here"
TEST_PASSWORD="Add your password here"

#These are very important, as this allows the login before every test run


### 5.Running Tests
Run all tests with dependency control:
pytest test_login.py -s  




