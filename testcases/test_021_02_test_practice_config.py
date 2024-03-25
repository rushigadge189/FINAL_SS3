from selenium import webdriver
from selenium.webdriver.common.by import By

from utilities.ReadConfig import ReadConfig
class Test_021_02_practise_auto_config():

    USERNAME=ReadConfig.getUserName() ;
    PASSWORD=ReadConfig.getPassWord() ;

    def test_021_02_pta_confog(self,setup):

        self.driver=setup ;

        self.driver.get("https://practicetestautomation.com/practice-test-login/") ;

        self.driver.find_element(By.XPATH, '//input[@name="username"]').send_keys(self.USERNAME) ;

        self.driver.find_element(By.XPATH, '//input[@type="password"]').send_keys(self.PASSWORD) ;

        self.driver.find_element(By.XPATH, '//button[@id="submit"]').click() ;

        if (self.driver.title=="Logged In Successfully | Practice Test Automation") :

            self.driver.save_screenshot("D:\\PYTHON CT15\\FINAL_REVISION\\screenshots\\test_021_02_test_pass.png") ;

            print("****************TEST IS PASSED***************") ;

            print("*************TEXT AFTER LOGIN*************") ;
            text1=self.driver.find_element(By.XPATH, '//strong[contains(text(), "Congratulations student")]').text ;
            print("\n", text1) ;

            self.driver.find_element(By.XPATH, '//a[@class="wp-block-button__link has-text-color has-background has-very-dark-gray-background-color"]').click() ;

            self.driver.close();
            assert True ;

        else:

            self.driver.save_screenshot("D:\\PYTHON CT15\\FINAL_REVISION\\screenshots\\test_021_02_test_fail.png") ;

            print("**************TEST IS FAILED****************") ;

            self.driver.close() ;
            assert False ;