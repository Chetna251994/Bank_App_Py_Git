from pageObjects.Login_Page import Login_Page_Class


class Test_Login_Param:

    def test_Login_BankApp_003(self, setup, GetDataForLogin):
        self.driver = setup

        self.lp = Login_Page_Class(self.driver)
        self.lp.Enter_Username(GetDataForLogin[0])
        self.lp.Enter_Password(GetDataForLogin[1])
        self.lp.Click_LoginButton()

        if self.lp.Validate_Login_Status() == "LoginPass" and GetDataForLogin[2] == "LoginPass":
            print("Login Pass")
        else:
            print("Login Fail")


