import unittest
from selenium import webdriver

class TEST_CASE_3959(unittest.TestCase):
    def set_up(self):
        driver = webdriver.Chrome()
        driver.get('')

    def login_successfully(self, username, pwd):
        self.login_page = SFLoginPage(self.driver)