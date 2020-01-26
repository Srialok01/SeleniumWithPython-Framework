from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
import logging
from Logger import custom_logger as cl
from Util import Utils
from Util.SeleniumDriver import SeleniumDriver


class Payment(SeleniumDriver):
    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    _creditCardRadioBTN_id = "paymentmethod_1"
    _paymentContinueBTN_xpath = "//input[@type='button'][@class='button-1 payment-method-next-step-button']"
    _cardholderName_id = "CardholderName"
    _cardNumber_xpath = "//input[@id='CardNumber']"
    _expirationMonth_xpath = "//select[@id='ExpireMonth']"
    _expirationYear_xpath = "//select[@id='ExpireYear']"
    _cVV_xpath = "//input[@id='CardCode']"
    _cardContinueBTN_xpath = "//input[@class='button-1 payment-info-next-step-button']"

    def clickOnCreditCardRadioBTN(self):
        self.waitForElement(self._creditCardRadioBTN_id, locatorType='id')
        self.elementClick(self._creditCardRadioBTN_id, locatorType='id')

    def clickOnPaymentContinueBTN(self):
        self.elementClick(self._paymentContinueBTN_xpath, locatorType='xpath')

    def enterCardDetails(self):
        self.sendKeys(Utils.CardHolderName, self._cardholderName_id, locatorType='id')
        self.sendKeys(Utils.CardNo, self._cardNumber_xpath, locatorType='xpath')
        WebElement_Month = self.driver.find_element_by_xpath(self._expirationMonth_xpath)
        select_Expdate = Select(WebElement_Month)
        select_Expdate.select_by_index(6)
        WebElement_Year = self.driver.find_element_by_xpath(self._expirationYear_xpath)
        select_ExpYear = Select(WebElement_Year)
        select_ExpYear.select_by_index(5)
        self.sendKeys(Utils.cvv, self._cVV_xpath, locatorType='xpath')
        self.elementClick(self._cardContinueBTN_xpath, locatorType='xpath')

    def PaymentOptions(self):
        self.driver.execute_script("window.scrollTo(0, 300);")
        self.clickOnCreditCardRadioBTN()
        self.clickOnPaymentContinueBTN()
        self.enterCardDetails()
