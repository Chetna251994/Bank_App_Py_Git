import time

from pageObjects.Login_Page import Login_Page_Class
from utilities.ReadConfig import ReadConfig_Class
from utilities.loggerfile import LogGenerator


class Test_Bank_Login:
    Username = ReadConfig_Class.getUsername()
    Password = ReadConfig_Class.getPassword()
    log = LogGenerator.loggen()


    def test_Bank_url_001(self, setup):
        # driver = webdriver.Chrome()
        # self.driver = setup
        self.driver = setup
        print("Driver.title--->" + self.driver.title)
        if self.driver.title == "Login":
            time.sleep(4)
            self.driver.save_screenshot(".\\Screenshots\\Screenshot_for_Pass.png")
            assert True
        else:
            self.driver.log("Test case is failed")
            self.driver.log("Taking th screenshot")
            self.driver.save_screenshot(".\\Screenshots\\Screenshot_for_Fail.png")
            assert False


    def test_Bank_Login_001(self, setup):
        # driver = webdriver.Chrome()
        self.driver = setup
        self.lp = Login_Page_Class(self.driver)
        self.driver.get("https://bankapp.credence.in/login.html")


        # self.driver.find_element(By.XPATH, "//input[@id='username']").send_keys("Chetna1")
        self.lp.Enter_Username(self.Username)


        # self.driver.find_element(By.XPATH, "//input[@id='password']").send_keys("Netra@1")
        self.lp.Enter_Password(self.Password)


        # self.driver.find_element(By.XPATH,"//button[@type='submit']").click()
        self.lp.Click_LoginButton()

        self.driver.quit()


