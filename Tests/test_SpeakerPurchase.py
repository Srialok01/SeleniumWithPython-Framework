import allure
import moment
import pytest

from Util import Utils
from Pages.CartPage import CartPage
from Pages.HomePage import HomePage
from Pages.Electronics_OthersPage import OtherItems
from Pages.LoginPage import LoginPage

from Pages.AddressPage import Address
from Pages.PaymentPage import Payment
from Pages.OrderConfirmationPage import OrderConfirmation
from Util.SeleniumDriver import SeleniumDriver
from Util.Utils import URL
import logging
from Logger import custom_logger as cl


#@pytest.mark.skip(" I don't want to execute this now")
@pytest.mark.usefixtures('test_setup')
class Test_SpeakerPurchase():
    try:

        log = cl.customLogger(logging.DEBUG)
        global ss_path, time
        ss_path = '/SpeakerPurchaseNewCustomer/'
        time = moment.now().strftime("%H-%M-%S_%d-%m-%Y")

        def test_01HomePage(self):
            driver = self.driver
            self.driver.get(URL)

            homeObj = HomePage(driver)
            title = homeObj.verifyHomePageLoad()
            assert title == True
            ss = SeleniumDriver(self.driver)
            ss.screenShot(Utils.whoami(), time, ss_path)
            homeObj.NavigateToOthers()
            ss = SeleniumDriver(self.driver)
            ss.screenShot(Utils.whoami(), time, ss_path)

        def test_02Speaker_buy(self):
            driver = self.driver
            cellObj = OtherItems(driver)
            cellObj.SelectSpeakers()
            ss = SeleniumDriver(self.driver)
            ss.screenShot(Utils.whoami(), time, ss_path)

        def test_03Cart_validations(self):
            driver = self.driver
            cartObj = CartPage(driver)
            cartObj.cart_validation()
            ss = SeleniumDriver(self.driver)
            ss.screenShot(Utils.whoami(), time, ss_path)

        def test_04Login(self):
            driver = self.driver
            loginObj = LoginPage(driver)
            loginObj.Checkout_as_Guest()
            ss = SeleniumDriver(self.driver)
            ss.screenShot(Utils.whoami(), time, ss_path)

        def test_05Address(self):
            driver = self.driver
            addressObj = Address(driver)
            addressObj.AddressInput()
            ss = SeleniumDriver(self.driver)
            ss.screenShot(Utils.whoami(), time, ss_path)

        def test_06Payment(self):
            driver = self.driver
            paymentObj = Payment(driver)
            paymentObj.PaymentOptions()
            ss = SeleniumDriver(self.driver)
            ss.screenShot(Utils.whoami(), time, ss_path)

        def test_07OrderConfirmation(self):
            driver = self.driver
            orderConfObj = OrderConfirmation(driver)
            orderConfObj.orderConfirmationdetails()
            ss = SeleniumDriver(self.driver)
            ss.screenShot(Utils.whoami(), time, ss_path)

    except AssertionError as error:
        print(error)