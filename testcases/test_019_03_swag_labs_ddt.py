from selenium import webdriver
from selenium.webdriver.common.by import By

from utilities import XUTils

class Test_19_03_sl_ddt():

    def test_019_03_swag_labs(self, setup):

        self.driver=setup ;

        path="D:\\PYTHON CT15\\FINAL_REVISION\\testdata\\SWAGLABS_LOGIN.xlsx" ;

        rows=XUTils.rowCount(path, 'Sheet1') ;

        for r in range (2, rows+1) :
            self.driver.get('https://www.saucedemo.com/') ;

            username=XUTils.readData(path, 'Sheet1', r, 1) ;
            password=XUTils.readData(path, 'Sheet1', r, 2) ;

            self.driver.find_element(By.XPATH, '//input[@placeholder="Username"]').send_keys(username) ;

            self.driver.find_element(By.XPATH, '//input[@placeholder="Password"]').send_keys(password) ;

            self.driver.find_element(By.XPATH, '//input[@id="login-button"]').click() ;

            try :

                self.driver.find_element(By.XPATH, '//button[@id="react-burger-menu-btn"]') ;

                print("\n*************TEST IS PASSED***************") ;

                self.driver.save_screenshot("D:\\PYTHON CT15\\FINAL_REVISION\\screenshots\\test_019_03_sl_pass.png") ;

                XUTils.writeData(path, 'Sheet1', r, 3, 'PASSED') ;

                self.driver.find_element(By.XPATH, '//button[@id="react-burger-menu-btn"]').click() ;

                self.driver.find_element(By.XPATH, '//a[@id="logout_sidebar_link"]').click() ;

            except :
                print("\n************TEST IS FAILED****************") ;

                XUTils.writeData(path, 'Sheet1', r, 3, 'FAILED') ;

                self.driver.save_screenshot("D:\\PYTHON CT15\\FINAL_REVISION\\screenshots\\test_019_03_sl_fail.png") ;

        self.driver.close() ;