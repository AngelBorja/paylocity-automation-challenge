"""
Tests:
- Add a new employee
- Edit employee details
- Delete employee and verify removal

Author: Angel
"""

import pytest
from playwright.sync_api import sync_playwright
from dotenv import load_dotenv
import os



def login(page):

    page.goto("https://wmxrwq14uc.execute-api.us-east-1.amazonaws.com/Prod/Account/LogIn")
    load_dotenv()
    USERNAME = os.getenv("TEST_USERNAME")
    PASSWORD = os.getenv("TEST_PASSWORD")
    page.fill("#Username", USERNAME)
    page.fill("#Password", PASSWORD)
    page.click("button[type='submit']")
    page.wait_for_url("**/Benefits")
    assert page.is_visible("#employeesTable")
    page.wait_for_selector("text=Net Pay")

@pytest.mark.dependency(name="add_user")
def test_addUser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        # Login and click on add button
        login(page)
        page.wait_for_selector("#employeesTable tr", timeout=3000)
        page.click("#add")

        # Change focus to modal and fill information to create user
        modal = page.locator("#employeeModal")
        modal.locator("text=Add Employee").wait_for()
        modal.locator("#firstName").fill("UserCreatedBy")
        modal.locator("#lastName").fill("APythonTest")
        modal.locator("#dependants").fill("1")
        modal.locator("#addEmployee").click()


        page.wait_for_selector("text=UserCreatedBy", timeout=3000)
        try:
            assert page.locator("td").all_text_contents().count("UserCreatedBy") > 0
        except AssertionError as e:
            page.screenshot(path="error_screenshot.png")
            raise 
        # After adding the user
        target_row = page.locator("tr:has(td:has-text('UserCreatedBy'))")
        user_id = target_row.locator("td").nth(0).text_content()

        # Save to file
        with open("user_id.txt", "w") as f:
            f.write(user_id)

@pytest.mark.dependency(depends=["add_user"], name="edit_user")
def test_editUser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        # Login once
        login(page)

        # Load User ID from file, Wait for the table to appear to click edit button
        with open("user_id.txt", "r") as f:
            user_id = f.read().strip()
        page.wait_for_selector(f"tr:has(td:has-text('{user_id}'))", timeout=5000)
        target_row = page.locator(f"tr:has(td:has-text('{user_id}'))")
        target_row.locator("i.fa-edit").first.click()

        # Change focus to modal and fill information to edit user
        modal = page.locator("#employeeModal")
        modal.locator("text=First Name:").wait_for()
        modal.locator("#firstName").fill("UserEditedBy")
        modal.locator("#lastName").fill("APythonEditUserTest")
        modal.locator("#dependants").fill("10")
        

        modal.locator("#updateEmployee").click()


        page.wait_for_selector("text=UserEditedBy", timeout=5000)
        try:
            assert page.locator("td").all_text_contents().count(f"{user_id}") > 0 
        except AssertionError as e:
            page.screenshot(path="error_screenshot.png")
            raise 


@pytest.mark.dependency(depends=["edit_user"])        
def test_deleteUser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        # Login once
        login(page)

        with open("user_id.txt", "r") as f:
            user_id = f.read().strip()

        # Wait for the table to appear to click delete buttoon
        page.wait_for_selector(f"tr:has(td:has-text('{user_id}'))", timeout=5000)

        initial_count = page.locator("#employeesTable tbody tr").count()

        target_row = page.locator(f"tr:has(td:has-text('{user_id}'))")
        target_row.locator("i.fa-times").first.click()

        
        # Change focus to the delete user modal, click delete button
        modal = page.locator("#deleteModal")
        modal.locator("button:has-text('Delete')").wait_for()
        modal.locator("#deleteEmployee").click()

        page.locator(f"tr:has(td:has-text('{user_id}'))").wait_for(state="detached", timeout=5000)
        final_count = page.locator("#employeesTable tbody tr").count()
        try:
            assert final_count == initial_count - 1
        except AssertionError as e:
            page.screenshot(path="error_screenshot.png")
            raise e
