from selenium.webdriver.common.by import By
from Pages.BasePage import BasePage


class LoginPage(BasePage):
    userName = (By.ID, "txtUsername")
    password = (By.ID, "txtPassword")
    loginBtn = (By.ID, "btnLogin")

    def __init__(self, driver):
        super().__init__(driver)

    def getPageTitle(self):
        return self.driver.title

    def login(self, un, pwd):
        self.driver.find_element(*self.userName).send_keys(un)
        self.driver.find_element(*self.password).send_keys(pwd)

    def clickLogin(self):
        self.driver.find_element(*self.loginBtn).click()




