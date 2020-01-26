from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import logging
from Logger import custom_logger as cl
from Util.SeleniumDriver import SeleniumDriver


class OrderConfirmation(SeleniumDriver):
    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    _confirmBTN_xpath = "//input[@class='button-1 confirm-order-next-step-button']"
    _orderNo_xpath = "//div[@class='order-number']/strong"

    def clickOnConfirmBTN(self):
        self.elementClick(self._confirmBTN_xpath, locatorType='xpath')

    def copyOrderNo(self):
        OrderNo = self.getElement(self._orderNo_xpath, locatorType='xpath').text
        # OrderNo = WebDriverWait(self.driver, 10).until(lambda x: x.find_element_(*OrderConfirmation.Order_No)).text
        print(OrderNo)
        text_file = open('C:/files/file.txt', 'a')
        text_file.writelines("\n" + OrderNo)
        text_file.close()

    def orderConfirmationdetails(self):
        self.driver.execute_script("window.scrollTo(0, 800);")
        self.clickOnConfirmBTN()
        self.copyOrderNo()
