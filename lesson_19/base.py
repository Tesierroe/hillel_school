class Base:

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get(self.URL)

    URL = "https://demoqa.com/automation-practice-form"
