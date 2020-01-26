import time

from Util.SeleniumDriver import SeleniumDriver
import logging
from Logger import custom_logger as cl


class LoginPage(SeleniumDriver):
    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    _email_id = "Email"
    _password_id = "Password"
    _loginBtn_xpath = "//input[@class ='button-1 login-button']"
    _checkoutasguest_BTN_xpath = "//input[@class ='button-1 checkout-as-guest-button']"

    def enterEmail(self, email):
        self.sendKeys(email, self._email_id, locatorType='id')

    def enterPasswordField(self, password):
        self.sendKeys(password, self._password_id, locatorType='id')
        # self.getPasswordField().send_keys(password)

    def clickOnLoginBtn(self):
        self.elementClick(self._loginBtn_xpath, locatorType='xpath')

    def clickOnGuestBtn(self):
        self.elementClick(self._checkoutasguest_BTN_xpath, locatorType='xpath')
        time.sleep(3)

    def Login(self, email, password):
        self.waitForElement(locator=self._email_id, locatorType='id')
        self.enterEmail(email)
        self.enterPasswordField(password)
        self.clickOnLoginBtn()

    def Checkout_as_Guest(self):
        self.clickOnGuestBtn()
