from selenium import webdriver
from selenium.webdriver.common.by import By


class TestUitap():
  def setup_method(self):
    self.driver = webdriver.Chrome()
    self.driver.get("http://uitestingplayground.com/home")
  
  def teardown_method(self):
    self.driver.quit()


  def test_dynamic_id(self):
    # Dynamic ID button check
    self.driver.find_element(By.LINK_TEXT, "Dynamic ID").click()
    self.driver.find_element(By.XPATH, "//body[1]/section[1]/div[1]/button[1]").click()
    self.driver.find_element(By.LINK_TEXT, "Home").click()

  def test_csd(self):
    # Client Side Delay button check
    self.driver.find_element(By.LINK_TEXT, "Client Side Delay").click()
    self.driver.find_element(By.ID, "ajaxButton").click()
    self.driver.get("http://uitestingplayground.com/home")

  def test_class_atr(self):
    # Class Attribute button check
    self.driver.find_element(By.LINK_TEXT, "Class Attribute").click()
    self.driver.find_element(By.CSS_SELECTOR, ".class2").click()


  def test_resources(self):
    # Checking the Resources tab and w3schools.com links exist
    self.driver.find_element(By.LINK_TEXT, "Resources").click()

    search_list = self.driver.find_elements(By.XPATH, "/html/body/section/div/ul/li/a")
    for item in search_list:
      if item.text == 'w3schools.com':
        item.click()
      break

    assert self.driver.find_element(By.CLASS_NAME, "learntocodeh1").text == 'Learn to Code'