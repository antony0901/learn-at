from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .locator import USER_NAME_INPUT, PWD_INPUT, LOGO, LOGIN_BTN

class SFLoginPage(BasePage):
    def is_located_on(self):
        return not self.driver.find_element_by_xpath(LOGO)
    
    def do_login(self, username, pwd):
        self.driver.find_element_by_xpath(USER_NAME_INPUT).send_keys(username)
        self.driver.find_element_by_xpath(PWD_INPUT).send_keys(pwd)
        login_btn = self.wait.until(EC.element_to_be_clickable(LOGIN_BTN))
        login_btn.click()
