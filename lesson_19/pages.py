import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from lesson_19.base import Base


class RegistrationForm(Base):

    NAME = (By.ID, "firstName")
    SURNAME = (By.ID, "lastName")
    EMAIL = (By.ID, "userEmail")
    NUMBER = (By.ID, "userNumber")
    GENDER = (By.CLASS_NAME, "custom-control-label")
    DATEPICKER = (By.ID, "dateOfBirthInput")
    SUBJECT = (By.ID, "subjectsInput")
    ADDRESS = (By.ID, "currentAddress")
    STATE = (By.ID, "react-select-3-input")
    CITY = (By.ID, "react-select-4-input")
    SUBMIT = (By.ID, "submit")

    def enter_name(self, name):
        self.driver.find_element(*self.NAME).send_keys(name)

    def enter_surname(self, surname):
        self.driver.find_element(*self.SURNAME).send_keys(surname)

    def enter_email(self, email):
        self.driver.find_element(*self.EMAIL).send_keys(email)

    def enter_phone(self, phone):
        self.driver.find_element(*self.NUMBER).send_keys(phone)

    def select_gender(self):
        self.driver.find_element(*self.GENDER).click()

    def enter_date(self, date):
        self.driver.find_element(*self.DATEPICKER).send_keys(date)
        blank_area = self.driver.find_element(By.TAG_NAME, "body")
        blank_area.click()

    def select_subject(self, subject):
        try:
            dropdown = self.driver.find_element(*self.SUBJECT)
            dropdown.send_keys(subject)
            dropdown.send_keys(Keys.ENTER)
        except NoSuchElementException:
            print("Subjects dropdown element not found on the page.")

    def select_hobbies(self, hobbies):
        for hobby in hobbies:
            self.driver.find_element(By.XPATH, "//label[text()='{}']".format(hobby)).click()

    def enter_address(self, address):
        self.driver.find_element(*self.ADDRESS).send_keys(address)

    def select_state(self, state):
        try:
            dropdown = self.driver.find_element(*self.STATE)
            dropdown.send_keys(state)
            dropdown.send_keys(Keys.ENTER)
        except NoSuchElementException:
            print("Subjects dropdown element not found on the page.")

    def select_city(self, city):
        try:
            dropdown = self.driver.find_element(*self.CITY)
            dropdown.send_keys(city)
            dropdown.send_keys(Keys.ENTER)
        except NoSuchElementException:
            print("Subjects dropdown element not found on the page.")

    def submit_form(self):
        self.driver.execute_script("document.body.style.zoom='70%'")
        dropdown = self.driver.find_element(*self.CITY)
        submit_button = self.driver.find_element(*self.SUBMIT)
        actions = ActionChains(self.driver)
        actions.move_to_element(dropdown).send_keys(Keys.TAB)
        actions.move_to_element(submit_button).send_keys(Keys.TAB)
        submit_button.send_keys(Keys.ENTER)

    def get_confirmation_message(self):
        wait = WebDriverWait(self.driver, 10)
        confirmation_element = wait.until(
            EC.visibility_of_element_located((By.XPATH, "//div[contains(text(), 'Thanks for submitting the form')]")))
        return confirmation_element.text

    def no_confirmation_message(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(
            EC.invisibility_of_element_located((By.XPATH, "//div[contains(text(), 'Thanks for submitting the form')]")))
        return True
