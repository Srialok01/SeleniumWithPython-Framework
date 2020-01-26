import time

from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
import logging
from Logger import custom_logger as cl
from Util.SeleniumDriver import SeleniumDriver


class CellPhonePage(SeleniumDriver):
    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    _NokiaPhone_id_Linktxt = "Nokia Lumia 1020"
    _AddToCartBTN_xpath = "//input[@type='button'][@id='add-to-cart-button-20']"
    _ShoppingCart_xpath = "//div[@class='header-links']//descendant::span[@class ='cart-label']"
    _ShoppingCart_Confirmation_xpath = "//div[@id='bar-notification']//span"
    _GoToCart_xpath = "//div[@class='buttons']/input[@value='Go to cart']"

    def clickOnNokiaPhone(self):
        self.waitForElement(self._NokiaPhone_id_Linktxt, locatorType='link')
        self.elementClick(self._NokiaPhone_id_Linktxt, locatorType='link')

    def clickOnAddtoCartBTN(self):
        self.waitForElement(self._AddToCartBTN_xpath, locatorType='xpath')
        self.elementClick(self._AddToCartBTN_xpath, locatorType='xpath')

    def clickOnShoppingCartConfirmationBTN(self):
        self.waitForElement(self._ShoppingCart_Confirmation_xpath, locatorType='xpath')
        self.elementClick(self._ShoppingCart_Confirmation_xpath, locatorType='xpath')

    def clickOnGoToCartBTN(self):
        self.elementClick(self._GoToCart_xpath, locatorType='xpath')

    def SelectPhone(self):
        self.clickOnNokiaPhone()
        self.driver.execute_script("window.scrollTo(0, 300);")
        self.clickOnAddtoCartBTN()
        self.clickOnShoppingCartConfirmationBTN()
        self.driver.execute_script("window.scrollTo(0, -400);")
        time.sleep(2)
        self.hoverOnElement(self._ShoppingCart_xpath, locatorType='xpath')
        self.clickOnGoToCartBTN()

