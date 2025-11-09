README.md
# 🧪 Playwright E2E Test Suite: Employee Management Flow

This repository contains an end-to-end test suite built with [Playwright](https://playwright.dev/python/) and `pytest` to automate the employee management flow of a sample HR platform. It covers:

- ➕ Add a new employee
- ✏️ Edit employee details
- ❌ Delete employee and verify removal


---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/your-username/playwright-employee-tests.git
cd playwright-employee-tests


2. Install dependencies
pip install -r requirements.txt


Required packages:
- playwright
- pytest
- pytest-dependency
- python-dotenv

3. Install Playwright browsers
playwright install



🔐 Environment Variables
Create a .env file in the project root:
TEST_USERNAME=TestUser831
TEST_PASSWORD=YK+vA5;*wVTO


You can copy from .env.example and customize as needed.


🧪 Running Tests
Run all tests with dependency control:
pytest


Generate an HTML report:
pytest --html=report.html --self-contained-html



📁 Test Structure
|  |  |  | 
| test_addUser |  |  | 
| test_editUser |  | add_user | 
| test_deleteUser |  | edit_user | 



📦 File Usage
- user_id.txt – Stores the ID of the created user for reuse across tests
- error_screenshot.png – Captures a screenshot if any assertion fails

🧠 Author
Built with ❤️ by Angel — focused on clean automation, modular flows, and robust validation.

📜 License
MIT License — feel free to fork, adapt, and build on top of it.
