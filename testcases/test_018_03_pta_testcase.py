from pageobjects.test_018_03_pta_pageobjects import Test_018_03_practice_test_auto
class Test_018_03_pta_test_cases():

    def test_018_03_pat_testcases(self,setup):

        self.driver=setup ;

        self.obj=Test_018_03_practice_test_auto(self.driver) ;

        self.obj.test_get("https://practicetestautomation.com/practice-test-login/") ;

        self.obj.test_enter_username('student') ;

        self.obj.test_enter_password('Password123') ;

        self.obj.test_click_login() ;

        if(self.obj.test_status()==True) :
            self.driver.save_screenshot("D:\\PYTHON CT15\\FINAL_REVISION\\screenshots\\test_018_03_pta_pass.png") ;

        else:
            self.driver.save_screenshot("D:\\PYTHON CT15\\FINAL_REVISION\\screenshots\\test_018_03_pta_fail.png") ;

        self.obj.test_print() ;

        self.obj.test_logout() ;

        self.driver.close() ;