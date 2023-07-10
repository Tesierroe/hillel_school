import allure
import pytest
from selenium import webdriver
from .pages import RegistrationForm


@allure.suite("Test Valid Registration")
@allure.title("Valid Registration Form")
@allure.severity(allure.severity_level.CRITICAL)
def test_valid_form():

    driver = webdriver.Chrome()
    driver.maximize_window()

    registration_page = RegistrationForm(driver)
    registration_page.open()

    registration_page.enter_name("John")
    registration_page.enter_surname("Doe")
    registration_page.enter_email("doe@sdds.com")
    registration_page.select_gender()
    registration_page.enter_phone("1234567890")
    registration_page.enter_date("2023-01-01")
    registration_page.select_subject("Computer Science")
    registration_page.select_hobbies(["Sports", "Reading", "Music"])
    registration_page.enter_address("123 Street, City")
    registration_page.select_state("NCR")
    registration_page.select_city("Delhi")
    registration_page.submit_form()
    assert registration_page.get_confirmation_message() == "Thanks for submitting the form"
    driver.quit()


@allure.suite("Test Invalid Registration")
@allure.title("Invalid Registration Form")
def test_invalid_form():

    driver = webdriver.Chrome()
    driver.maximize_window()

    registration_page = RegistrationForm(driver)
    registration_page.open()

    registration_page.enter_name("   ")
    registration_page.enter_surname("   ")
    registration_page.enter_email("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa@sdds.com")
    registration_page.select_gender()
    registration_page.enter_phone("0000000000")
    registration_page.enter_date("1900-01-01")
    registration_page.submit_form()
    assert registration_page.get_confirmation_message() == "Thanks for submitting the form"
    driver.quit()


@allure.suite("Test Empty Registration")
@allure.title("Empty Registration Form")
def test_empty_form():

    driver = webdriver.Chrome()
    driver.maximize_window()

    registration_page = RegistrationForm(driver)
    registration_page.open()

    registration_page.submit_form()
    assert registration_page.no_confirmation_message()
    driver.quit()


if __name__ == "__main__":
    pytest.main([__file__, "--alluredir=result"])
