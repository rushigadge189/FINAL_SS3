from selenium import webdriver
from selenium.webdriver.common.by import By

from utilities.ReadConfig import ReadConfig ;


class Test_021_03_heroku_configureation():

    USERNAME=ReadConfig.getUserName() ;
    PASSWORD=ReadConfig.getPassWord() ;

    def test_021_03_heroku(self, setup):

        self.driver=setup ;

        self.driver.get("https://the-internet.herokuapp.com/login") ;

        self.driver.find_element(By.XPATH, '//input[@name="username"]').send_keys(self.USERNAME) ;

        self.driver.find_element(By.XPATH, '//input[@type="password"]').send_keys(self.PASSWORD) ;

        self.driver.find_element(By.XPATH, '//i[text()=" Login"]').click() ;

        try :

            self.driver.find_element(By.XPATH, '//a[@class="button secondary radius"]') ;

            self.driver.save_screenshot("D:\PYTHON CT15\FINAL_REVISION\screenshots\\test_021_03_heroku_pass.png") ;

            print("\n***************TEST IS PASSED**************") ;

            print("\n***************TEXT AFTER LOGIN*************");
            text1=self.driver.find_element(By.XPATH, '//h4[@class="subheader"]').text ;
            print("\n", text1) ;

            self.driver.find_element(By.XPATH, '//a[@class="button secondary radius"]').click() ;

            self.driver.close() ;
            assert True ;

        except :

            self.driver.save_screenshot("D:\PYTHON CT15\FINAL_REVISION\screenshots\\test_021_03_heroku_fail.png") ;

            print("\n****************TEST IS FAILED**************") ;

            self.driver.close() ;
            assert False ;