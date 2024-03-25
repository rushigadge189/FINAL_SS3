import time

from selenium import webdriver
from selenium.webdriver.common.by import By

from utilities import XUTils

class Test_019_02_pa_ddt():

    def test_019_02_pr_auto_ddt(self, setup):

        self.driver=setup ;

        path="D:\\PYTHON CT15\\FINAL_REVISION\\testdata\\AUTOMATION_PRACTISE_LOGIN.xlsx" ;

        rows=XUTils.rowCount(path, 'Sheet1') ;

        for r in range (2, rows+1) :

            self.driver.get("https://practicetestautomation.com/practice-test-login/") ;

            username=XUTils.readData(path, 'Sheet1', r, 1) ;
            password=XUTils.readData(path, 'Sheet1', r, 2) ;

            self.driver.find_element(By.XPATH, '//input[@id="username"]').send_keys(username) ;

            self.driver.find_element(By.XPATH, '//input[@name="password"]').send_keys(password) ;

            self.driver.find_element(By.XPATH, '//button[@id="submit"]').click() ;

            if (self.driver.title=="Logged In Successfully | Practice Test Automation"):
                print("\n**************TEST IS PASSED***************") ;
                XUTils.writeData(path, 'Sheet1', r, 3, 'PASSED') ;

                self.driver.save_screenshot("D:\\PYTHON CT15\\FINAL_REVISION\\screenshots\\test_019_pa_pass.png") ;

                print1=self.driver.find_element(By.XPATH, '//strong[contains(text(), "Congratulations student. You successfully logged in!")]').text ;
                print("\n************TEXT AFTER LOGIN************") ;
                print("\n", print1) ;

                self.driver.find_element(By.XPATH, '//a[text()="Log out"]').click() ;
                time.sleep(1) ;

            else:
                print("\n**************TEST IS FAILED************") ;

                self.driver.save_screenshot("D:\\PYTHON CT15\\FINAL_REVISION\\screenshots\\test_019_pa_fail.png");

                XUTils.writeData(path, 'Sheet1', r, 3, 'FAILED') ;

        self.driver.close() ;