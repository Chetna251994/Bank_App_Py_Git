# from selenium.webdriver.common.by import By
#
#
# class LoginPage_Class:
#     LoginText_XPATH = (By.XPATH, "//a[normalize-space()='Login']")
#     UserName_Xpath = (By.XPATH, "//input[@id='username']")
#     Password_XPATH = (By.XPATH, "//input[@id='password']")
#     Click_LoginButt_XPATH = (By.XPATH, "//button[@type='submit']")
#
#
#     def __init__(self, driver):
#         self.driver = driver
#
#     def LoginClick(self, click):
#         self.driver.find_element(*LoginPage_Class.LoginText_XPATH).Click()
#
#     def Enter_UserName(self, username):
#         self.driver.find_element(*LoginPage_Class.UserName_Xpath).send_keys(username)
#
#     def Enter_Password(self, password):
#         self.driver.find_element(*LoginPage_Class.Password_XPATH).send_keys(password)
#
#     def Click_LoginButton(self):
#         self.driver.find_element(*LoginPage_Class.Click_LoginButt_XPATH).click()
#
#
import time

from selenium.webdriver.common.by import By


class Login_Page_Class:

    Text_Username = (By.XPATH, "//input[@id='username']")
    Text_Password = (By.XPATH, "//input[@id='password']")
    Click_Login = (By.XPATH, "//button[@type='submit']")
    Logout_Button = (By.XPATH, "//a[normalize-space()='Logout']")



    def __init__(self, setup):
        self.driver = setup

    def Enter_Username(self, username):
        self.driver.find_element(*Login_Page_Class.Text_Username).send_keys(username)

    def Enter_Password(self, password):
        self.driver.find_element(*Login_Page_Class.Text_Password).send_keys(password)

    def Click_LoginButton(self):
        self.driver.find_element(*Login_Page_Class.Click_Login).click()

    def Click_LogoutButton(self):
        self.driver.find_element(*Login_Page_Class.Logout_Button).click()


    def Validate_Login_Status(self):
        try:
            time.sleep(2)
            self.driver.find_element(*Login_Page_Class.Logout_Button).click()
            print("Test case passed")
            return "LoginPass"
        except:
            print("Test case Failed")
            return "LoginFail"










