import logging
from Logger import custom_logger as cl
from Util.SeleniumDriver import SeleniumDriver


class CartPage(SeleniumDriver):
    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    _cartQuantity = "//td[@class='quantity']//input[@class='qty-input']"
    _terms_And_conditions_id = "termsofservice"
    _checkoutBTN_id = "checkout"

    def cart_validation(self):
        self.driver.execute_script("window.scrollTo(0, 400);")
        self.waitForElement(self._terms_And_conditions_id, locatorType='id')
        self.elementClick(self._terms_And_conditions_id, locatorType='id')
        self.elementClick(self._checkoutBTN_id,locatorType='id')

        # WebDriverWait(self.driver, 10).until(lambda x: x.find_element(*CartPage.Terms_And_conditions)).click()
        # self.driver.find_element(*CartPage.CheckoutBTN).click()
