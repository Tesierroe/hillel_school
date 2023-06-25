from selenium import webdriver
from selenium.common import ElementNotVisibleException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
import allure

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
wait = WebDriverWait(driver, timeout=10, poll_frequency=1, ignored_exceptions=[ElementNotVisibleException])

@allure.story('Test flow for XYZ Bank')
class TestXyzBank():

    def setup_method(self):
        driver.get('https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login')

    def teardown_method(self):
        driver.quit()

    @allure.description('User is navigated to XYZ Bank web app. The user logs in as a manager')
    @allure.title('Check Bank manager login flow')
    def test_bank_manager_login(self):

        #'Bank Manager Login button check'
        wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text() = 'Bank Manager Login']"))).click()

        #'Add Customer button check'
        wait.until(EC.element_to_be_clickable((By.XPATH, '//body/div[1]/div[1]/div[2]/div[1]/div[1]/button[1]'))).click()

        #'First Name feild check'
        wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/div[2]/div/div[2]/div/div/form/div[1]/input'))).send_keys("Jane")

        #'Last Name feild check'
        wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/div[2]/div/div[2]/div/div/form/div[2]/input'))).send_keys("N")

        #'Postal Code check'
        wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/div[2]/div/div[2]/div/div/form/div[3]/input'))).send_keys("23434")

        #'Submit button check'
        wait.until(EC.element_to_be_clickable((By.XPATH, '//body/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/form[1]/button[1]'))).click()

        assert driver.switch_to.alert.text == "Customer added successfully with customer id :6"









