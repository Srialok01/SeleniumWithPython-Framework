import inspect

import allure

URL="https://demo.nopcommerce.com/"

Email = "aloksri2204@gmail.com"
Password = "Test123"


# WhoAmI function returns the name of function called
def whoami():
    return inspect.stack()[1][3]


# Card details
CardHolderName = "Alok Srivastava"
CardNo = "6331101999990016"
cvv = "123"

# Address details

dict_address = {'First_Name': "Alok",
                'Last_Name': "Srivastava",
                'Guest_Email': "abc@gmail.com",
                'City': "Pune",
                'Address1': "Kharadi",
                'PostCode': "411014",
                'PhoneNo': "9415862204"
                }


def screenShot(self, testName, time, ss_path):
    """
    Takes screenshot of the current open web page
    """
    directory = "Screenshots"
    ScreenShotName = testName + time
    path = ss_path + ScreenShotName + ".png"
    self.driver.get_screenshot_as_file(directory + path)
    allure.attach(self.driver.get_screenshot_as_png(), name=ScreenShotName,
                  attachment_type=allure.attachment_type.PNG)
    # try:
    #     if not os.path.exists(destinationDirectory):
    #         os.makedirs(destinationDirectory)
    #     self.driver.save_screenshot(destinationFile)
    #     self.log.info("Screenshot save to directory: " + destinationFile)
    # except:
    #     self.log.error("### Exception Occurred when taking screenshot")
    #     print_stack()
