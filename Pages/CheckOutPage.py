import logging
from Logger import custom_logger as cl
from Util.SeleniumDriver import SeleniumDriver


class CheckOut(SeleniumDriver):
    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    _terms_And_conditions_id = "termsofservice"
    _checkoutBTN_id = "checkout"

    def Check_out(self):
        self.driver.execute_script("window.scrollTo(0, 400);")
        self.waitForElement(self._terms_And_conditions_id, locatorType='id')
        self.elementClick(self._terms_And_conditions_id, locatorType='id')
        self.elementClick(self._checkoutBTN_id, locatorType='id')
