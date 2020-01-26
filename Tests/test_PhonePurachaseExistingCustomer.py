import moment
import pytest
from Util import Utils
from Pages.CartPage import CartPage
from Pages.HomePage import HomePage
from Pages.Electronics_CellPhonePage import CellPhonePage
from Pages.LoginPage import LoginPage
from Pages.CheckOutPage import CheckOut
from Pages.AddressPage import Address
from Pages.PaymentPage import Payment
from Pages.OrderConfirmationPage import OrderConfirmation
from Util.SeleniumDriver import SeleniumDriver


# @pytest.mark.skip("I don't want to execute this now")


@pytest.mark.usefixtures('test_setup')
class Test_PhonePurchaseExistingCustomer:
    try:

        global ss_path, time
        ss_path = '/PhonePurchaseExistingCustomer/'

        time = moment.now().strftime("%H-%M-%S_%d-%m-%Y")

        def test_01HomePage(self):

            homeObj = HomePage(self.driver)

            title = homeObj.verifyHomePageLoad()
            assert title == True
            homeObj.NavigateToCellPhone()

            ss = SeleniumDriver(self.driver)
            ss.screenShot(Utils.whoami(), time, ss_path)

        def test_02Phone_buy(self):
            driver = self.driver
            cellObj = CellPhonePage(driver)
            cellObj.SelectPhone()
            ss = SeleniumDriver(self.driver)
            ss.screenShot(Utils.whoami(), time, ss_path)
            title_PhonePage = driver.title
            assert title_PhonePage == 'nopCommerce demo store. Shopping Cart', 'Page not loaded'

        def test_03Cart_validations(self):
            driver = self.driver
            cartObj = CartPage(driver)
            cartObj.cart_validation()
            ss = SeleniumDriver(self.driver)
            ss.screenShot(Utils.whoami(), time, ss_path)
            title_PhonePage = driver.title
            assert title_PhonePage == 'nopCommerce demo store. Login', 'Page not loaded'

        def test_04Login(self):
            driver = self.driver
            loginObj = LoginPage(driver)
            loginObj.Login(Utils.Email, Utils.Password)
            ss = SeleniumDriver(self.driver)
            ss.screenShot(Utils.whoami(), time, ss_path)
            title_PhonePage = driver.title
            assert title_PhonePage == 'nopCommerce demo store. Shopping Cart', 'Page not loaded'

        def test_05Checkout(self):
            driver = self.driver
            checkoutObj = CheckOut(driver)
            checkoutObj.Check_out()
            ss = SeleniumDriver(self.driver)
            ss.screenShot(Utils.whoami(), time, ss_path)

        def test_06Address(self):
            driver = self.driver
            addressObj = Address(driver)
            testName = Utils.whoami()
            ss = SeleniumDriver(self.driver)
            ss.screenShot(testName, time, ss_path)
            addressObj.continueAddress()
            ss.screenShot(Utils.whoami(), time, ss_path)

        def test_07Payment(self):
            driver = self.driver
            paymentObj = Payment(driver)
            paymentObj.PaymentOptions()
            ss = SeleniumDriver(self.driver)
            ss.screenShot(Utils.whoami(), time, ss_path)

        def test_08OrderConfirmation(self):
            driver = self.driver
            orderConfObj = OrderConfirmation(driver)
            orderConfObj.orderConfirmationdetails()
            ss = SeleniumDriver(self.driver)
            ss.screenShot(Utils.whoami(), time, ss_path)

    except AssertionError as error:
        print(error)
