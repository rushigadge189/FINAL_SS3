import time

from selenium import webdriver
from selenium.webdriver.common.by import By


class Test_017_fixture_conf():

    def test_17_01_url(self,setup):

        self.driver=setup;

        self.driver.get('https://practice.expandtesting.com/login') ;
        time.sleep(1) ;

        if (self.driver.title=='Test Automation Practice: Working with Login form') :
            self.driver.save_screenshot("D:\\PYTHON CT15\\FINAL_REVISION\\screenshots\\test_17_01_url_pass.png") ;

            print ('\n---------------------YOU ARE AT THE RIGHT PAGE----------------') ;

            self.driver.close() ;
            assert True ;

        else:
            self.driver.save_screenshot("D:\\PYTHON CT15\\FINAL_REVISION\\screenshots\\test_17_01_url_fail.png");

            print ('\n-------------------SORRY, SOMETHING WENT WRONG-----------------') ;

            self.driver.close();
            assert False ;

    def test_017_02_login(self, setup):

        self.driver=setup ;

        self.driver.get('https://practice.expandtesting.com/login') ;
        time.sleep(1) ;

        self.driver.find_element(By.XPATH, '//input[@name="username"]').send_keys('practice') ;
        time.sleep(1) ;

        self.driver.find_element(By.XPATH, '//input[@name="password"]').send_keys('SuperSecretPassword!') ;
        time.sleep(1) ;

        self.driver.find_element(By.XPATH, '//button[text()="Login"]').click() ;
        time.sleep(1) ;

        try:
            time.sleep(1) ;

            self.driver.find_element(By.XPATH, '//h1[contains(text(), "Secure Area")]') ;

            self.driver.save_screenshot("D:\\PYTHON CT15\\FINAL_REVISION\\screenshots\\test_017_02_login_pass.png") ;

            print("\n--------------LOGIN SUCCESSFUL--------------") ;

            text1=self.driver.find_element(By.XPATH, '//h4[@class="subheader"]').text ;
            print("\n----------------TEXT AFTER LOGIN----------------")
            print("\n", text1) ;
            time.sleep(1) ;

            self.driver.find_element(By.XPATH, '//i[text()=" Logout"]').click() ;
            time.sleep(1) ;

            self.driver.close() ;
            assert True ;

        except:

            self.driver.save_screenshot("D:\\PYTHON CT15\\FINAL_REVISION\\screenshots\\test_017_02_login_pass.png");

            print("\n---------------SORRY, UNABLE TO LOGIN----------------") ;

            self.driver.close() ;
            assert False ;