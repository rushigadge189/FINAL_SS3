from pageobjects.test_018_01_ohrm_pages import Test_orangehrm_pages
class Test_18_01_ohrm_test_case():


    def test_18_01_orange_hrm(self,setup):

        self.driver=setup ;

        self.obj=Test_orangehrm_pages(self.driver) ;

        self.obj.test_get_url("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login") ;

        self.obj.test_enter_username('Admin') ;

        self.obj.test_enter_password('admin123') ;

        self.obj.test_click_login() ;

        if (self.obj.test_status()==True):
            self.driver.save_screenshot("D:\\\PYTHON CT15\\FINAL_REVISION\\\screenshots\\test_018_01_ohrm_pass.png") ;

        else:
            self.driver.save_screenshot("D:\\\PYTHON CT15\\FINAL_REVISION\\\screenshots\\test_018_01_ohrm_pass.png") ;

        self.obj.test_click_menu_tab();

        self.obj.test_click_logout() ;

        self.driver.close() ;



