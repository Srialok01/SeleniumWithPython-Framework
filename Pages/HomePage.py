import logging
from Logger import custom_logger as cl
from Util.SeleniumDriver import SeleniumDriver


class HomePage(SeleniumDriver):
    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    _electronics_xpath = "//ul[@class='top-menu notmobile']//a[contains(text(),'Electronics ')]"
    _cellphone_xpath = "//ul[@class='top-menu notmobile']//a[contains(text(),'Cell phones')]"
    _others_xpath = "//ul[@class='top-menu notmobile']//a[contains(text(),'Others')]"


    def NavigateToCellPhone(self):
        self.hoverOnElement(self._electronics_xpath, locatorType='xpath')
        self.elementClick(self._cellphone_xpath, locatorType='xpath')

    def NavigateToOthers(self):
        self.hoverOnElement(self._electronics_xpath, locatorType='xpath')
        self.elementClick(self._others_xpath, locatorType='xpath')

    def verifyHomePageLoad(self):
        if 'nopCommerce demo store' in self.getTitle():
            return True
        else:
            return False


