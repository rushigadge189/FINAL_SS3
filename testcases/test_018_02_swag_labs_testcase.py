import time

from pageobjects.test_018_02_swaglabs_pages import Test_swaglabspages
class Test_swaglab_case():

    def test_018_02_sl_tc(self,setup):

        self.driver=setup ;

        self.obj=Test_swaglabspages(self.driver) ;

        self.obj.test_get_url("https://www.saucedemo.com/") ;

        self.obj.test_enter_username('standard_user') ;

        self.obj.test_enter_pasword('secret_sauce') ;

        self.obj.test_click_login() ;

        if(self.obj.test_status()==True):
            self.driver.save_screenshot("D:\\PYTHON CT15\\FINAL_REVISION\\screenshots\\test_018_02_sl_pass.png") ;
        else :
            self.driver.save_screenshot("D:\\PYTHON CT15\\FINAL_REVISION\\screenshots\\test_018_02_sl_fail.png") ;

        self.obj.test_ham_bur_icon_click() ;

        self.obj.test_logout_click() ;

        self.driver.close() ;
