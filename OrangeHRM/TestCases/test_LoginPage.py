import time
from Pages.LoginPage import LoginPage
from TestCases.test_base import BaseTest
from Utilities.ConfigReader import get_property


class Test_Login(BaseTest):

    def test_login(self):
        self.lp = LoginPage(self.driver)
        self.lp.login(get_property("email"), get_property("password"))
        self.lp.clickLogin()

    def test_verifyHomePageTitle(self):
        self.lp = LoginPage(self.driver)
        self.lp.login(get_property("email"), get_property("password"))
        self.lp.clickLogin()
        time.sleep(2)
        title = self.lp.getPageTitle()
        if title == "OrangeHRM":
            assert True
        else:
            assert False
