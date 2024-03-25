from pageobjects.test_018_04_heroku_login_pages import Test_018_04_herko_pages

class Test_018_04_hk_login():

    def test_18_04_her_ku_login_test(self,setup):

        self.driver=setup ;

        self.obj=Test_018_04_herko_pages(self.driver) ;

        self.obj.test_get_url('https://the-internet.herokuapp.com/login') ;

        self.obj.test_enter_username('tomsmith');

        self.obj.test_enter_password('SuperSecretPassword!') ;

        self.obj.test_login() ;

        if(self.obj.test_status()==True):
            self.driver.save_screenshot("D:\\PYTHON CT15\\FINAL_REVISION\\\screenshots\\test_018_04_herku_pass.png") ;

        else:
            self.driver.save_screenshot("D:\\PYTHON CT15\\FINAL_REVISION\\\screenshots\\test_018_04_herku_fail.png");

        self.obj.test_print_text_after_login() ;

        self.obj.test_logout() ;
