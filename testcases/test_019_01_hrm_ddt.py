import time

from selenium import webdriver
from selenium.webdriver.common.by import By

from utilities import XUTils
class Test_019_orangehrm_ddt():

    def test_019_ohrm_ddt(self):

        driver=webdriver.Chrome() ;
        time.sleep(1) ;

        driver.maximize_window() ;
        time.sleep(1) ;

        driver.implicitly_wait(10) ;

        path="D:\\PYTHON CT15\\FINAL_REVISION\\testdata\\ORANGE_HRM_LOGIN.xlsx" ;

        rows=XUTils.rowCount(path, 'Sheet1') ;

        for r in range(2, rows+1) :

            driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login");
            time.sleep(1) ;

            username=XUTils.readData(path, 'Sheet1', r, 1) ;
            password=XUTils.readData(path, 'Sheet1', r, 2) ;

            driver.find_element(By.XPATH, '//input[@name="username"]').send_keys(username) ;
            time.sleep(1) ;

            driver.find_element(By.XPATH, '//input[@name="password"]').send_keys(password) ;
            time.sleep(1) ;

            driver.find_element(By.XPATH, '//button[@type="submit"]').click() ;
            time.sleep(1) ;

            try:

                driver.find_element(By.XPATH, '//p[@class="oxd-userdropdown-name"]') ;

                print("\n*****************TEST IS PASSED*******************") ;
                XUTils.writeData(path, 'Sheet1', r, 3, 'PASSED') ;

                driver.find_element(By.XPATH, '//p[@class="oxd-userdropdown-name"]').click() ;
                time.sleep(1) ;

                driver.find_element(By.XPATH, '//a[text()="Logout"]').click() ;
                time.sleep(1) ;

            except:

                print("\n*********************TEST IS FAILED*****************") ;
                XUTils.writeData(path, 'Sheet1', r, 3, 'FAILED') ;


        driver.close() ;
