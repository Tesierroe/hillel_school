from selenium import webdriver
from selenium.webdriver.common.by import By
import allure

@allure.story('Test flow for TheInternet')
class TestTheInternet:
    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.vars = {}

    def teardown_method(self):
        self.driver.quit()

    @allure.description('User is navigated to TheInternet web app. The user performs few steps to check links')
    @allure.title('Check Add/Remove, Checkboxes, Inputs, Status Codes, Typos, Notification Messages')

    def test_the_internet(self):

        #'Check Add/Remove Elements'
        self.driver.get("http://the-internet.herokuapp.com/")
        self.driver.find_element(By.LINK_TEXT, "Add/Remove Elements").click()

        assert self.driver.find_element(By.CSS_SELECTOR, "button").text == 'Add Element'
        self.driver.find_element(By.CSS_SELECTOR, "button").click()

        assert self.driver.find_element(By.CSS_SELECTOR, ".added-manually").text == 'Delete'
        self.driver.find_element(By.CSS_SELECTOR, ".added-manually").click()
        self.driver.get("http://the-internet.herokuapp.com/")

        #'Check Checkboxes'
        self.driver.find_element(By.LINK_TEXT, "Checkboxes").click()
        self.driver.find_element(By.XPATH, '//*[@id="checkboxes"]/input[1]').click()
        assert self.driver.find_element(By.XPATH, '//*[@id="checkboxes"]/input[1]').is_selected()
        self.driver.get("http://the-internet.herokuapp.com/")

        #'Check Inputs'
        self.driver.find_element(By.LINK_TEXT, "Inputs").click()
        self.driver.find_element(By.CSS_SELECTOR, "input").click()
        assert self.driver.find_element(By.CSS_SELECTOR, "input").is_enabled()
        self.driver.find_element(By.CSS_SELECTOR, "input").send_keys("333")
        self.driver.get("http://the-internet.herokuapp.com/")

        #'Check Status Codes'
        self.driver.find_element(By.LINK_TEXT, "Status Codes").click()
        assert self.driver.find_element(By.LINK_TEXT, "500").text == '500'
        self.driver.find_element(By.LINK_TEXT, "500").click()
        self.driver.find_element(By.LINK_TEXT, "here").click()
        self.driver.get("http://the-internet.herokuapp.com/")

        #'Check Typos'
        self.driver.find_element(By.LINK_TEXT, "Typos").click()
        self.driver.get("http://the-internet.herokuapp.com/")

        #'Check Notification Messages'
        self.driver.find_element(By.LINK_TEXT, "Notification Messages").click()
        assert self.driver.find_element(By.LINK_TEXT, "Click here").is_enabled()
