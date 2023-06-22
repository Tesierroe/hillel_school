from selenium import webdriver
from selenium.common import ElementNotVisibleException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
wait = WebDriverWait(driver, timeout=10, poll_frequency=1, ignored_exceptions=[ElementNotVisibleException])


class TestXyzBank():

    def setup_method(self):
        driver.get('https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login')

    def teardown_method(self):
        driver.quit()

    def test_bank_manager_login(self):

        # Bank Manager Login button
        wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text() = 'Bank Manager Login']"))).click()

        # Add Customer button
        wait.until(EC.element_to_be_clickable((By.XPATH, '//body/div[1]/div[1]/div[2]/div[1]/div[1]/button[1]'))).click()

        # First Name
        wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/div[2]/div/div[2]/div/div/form/div[1]/input'))).send_keys("Jane")

        # Last Name
        wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/div[2]/div/div[2]/div/div/form/div[2]/input'))).send_keys("N")

        # Postal Code
        wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/div[2]/div/div[2]/div/div/form/div[3]/input'))).send_keys("23434")

        # Submit button
        wait.until(EC.element_to_be_clickable((By.XPATH, '//body/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/form[1]/button[1]'))).click()

        assert driver.switch_to.alert.text == "Customer added successfully with customer id :6"









