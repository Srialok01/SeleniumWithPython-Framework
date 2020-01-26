import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from Util import Utils
import logging
from Logger import custom_logger as cl
from Util.SeleniumDriver import SeleniumDriver


class Address(SeleniumDriver):
    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    _FirstName_id = 'BillingNewAddress_FirstName'
    _LastName_id = 'BillingNewAddress_LastName'
    _Email_id = 'BillingNewAddress_Email'
    _Country_xpath = "//Select[@id= 'BillingNewAddress_CountryId']"
    _State_xpath = "BillingNewAddress_StateProvinceId"
    _City_id = 'BillingNewAddress_City'
    _AddressLine_id = "BillingNewAddress_Address1"
    _Postcode_id = 'BillingNewAddress_ZipPostalCode'
    _PhoneNo_id = 'BillingNewAddress_PhoneNumber'
    _BillingAddressBTN_xpath = "//div[@id='billing-buttons-container']//input"
    _ShippingAddressBTN_xpath = "//input[@class='button-1 shipping-method-next-step-button']"

    def setFirstName(self):
        self.sendKeys(Utils.dict_address.get('First_Name'), self._FirstName_id, locatorType='id')

    def setLastName(self):
        self.sendKeys(Utils.dict_address.get('Last_Name'), self._LastName_id, locatorType='id')

    def setEmailId(self):
        self.sendKeys(Utils.dict_address.get('Guest_Email'), self._Email_id, locatorType='id')

    def selectCountry(self):
        WebElement_Country = self.driver.find_element(By.XPATH, self._Country_xpath)
        select_Country = Select(WebElement_Country)
        select_Country.select_by_value("133")

    def setCity(self):
        self.sendKeys(Utils.dict_address.get('City'), self._City_id, locatorType='id')

    def setAddressLine(self):
        self.sendKeys(Utils.dict_address.get('Address1'), self._AddressLine_id, locatorType='id')

    def setPostcode(self):
        self.sendKeys(Utils.dict_address.get('PostCode'), self._Postcode_id, locatorType='id')

    def setPhone(self):
        self.sendKeys(Utils.dict_address.get('PhoneNo'), self._PhoneNo_id, locatorType='id')

    def clickOnBillingAddressBTN(self):
        self.waitForElement(self._BillingAddressBTN_xpath, locatorType='xpath')
        self.elementClick(self._BillingAddressBTN_xpath, locatorType='xpath')

    def clickOnShippingAddressBTN(self):
        self.waitForElement(self._ShippingAddressBTN_xpath, locatorType='xpath')
        self.elementClick(self._ShippingAddressBTN_xpath, locatorType='xpath')

    def continueAddress(self):
        self.elementClick(self._BillingAddressBTN_xpath, locatorType='xpath')
        self.driver.execute_script("window.scrollTo(0, 300);")
        self.elementClick(self._ShippingAddressBTN_xpath, locatorType='xpath')

    def AddressInput(self):
        time.sleep(2)
        self.setFirstName()
        self.setLastName()
        email = self.driver.find_element(By.ID, self._Email_id)
        scrollToEmail = email.location_once_scrolled_into_view
        self.setEmailId()
        self.selectCountry()
        self.setCity()
        self.setAddressLine()
        self.setPostcode()
        self.setPhone()
        self.clickOnBillingAddressBTN()
        self.clickOnShippingAddressBTN()
