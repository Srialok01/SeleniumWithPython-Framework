from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
import logging
from Logger import custom_logger as cl
from Util.SeleniumDriver import SeleniumDriver


class OtherItems(SeleniumDriver):
    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    _soundSpeaker_link = "Portable Sound Speakers"
    _addToCart_xpath = "//input[@id='add-to-cart-button-23']"
    _shoppingCart_xpath = "//div[@class='header-links']//descendant::span[@class ='cart-label']"
    _shoppingCart_ConfirmationPopUp_xpath = "//div[@id='bar-notification']//span"
    _goToCart_xpath = "//div[@class='buttons']/input[@value='Go to cart']"

    def selectSpeaker(self):
        self.waitForElement(self._soundSpeaker_link, locatorType='link')
        self.elementClick(self._soundSpeaker_link, locatorType='link')

    def addtoCart(self):
        self.waitForElement(self._addToCart_xpath, locatorType='xpath')
        self.elementClick(self._addToCart_xpath, locatorType='xpath')

    def clickOnConfirmationPopUp(self):
        self.waitForElement(self._shoppingCart_ConfirmationPopUp_xpath, locatorType='xpath')
        self.elementClick(self._shoppingCart_ConfirmationPopUp_xpath, locatorType='xpath')

    def SelectSpeakers(self):
        self.selectSpeaker()
        self.driver.execute_script("window.scrollTo(0, 400);")
        self.addtoCart()
        self.clickOnConfirmationPopUp()
        self.driver.execute_script("window.scrollTo(0, -300);")
        self.hoverOnElement(self._shoppingCart_xpath, locatorType='xpath')
        self.elementClick(self._goToCart_xpath, locatorType='xpath')
    #
    # def Hover(self):
    #     hoverElement = WebDriverWait(self.driver, 10).until(lambda x: x.find_element(*OtherItems.ShoppingCart))
    #     hover = ActionChains(self.driver)
    #     hover.move_to_element(hoverElement).perform()
    #     self.driver.find_element(*OtherItems.GoToCart).click()
