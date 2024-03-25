import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from utilities.logger import Test_LogGenerator

class Test_20_01_ohrm():

    log=Test_LogGenerator.logger() ;


    def test_20_01_orange_hrm(self):

        self.log.info("TEST CASE IS STARTED") ;

        self.log.info("OPEN THE BROWSER") ;
        driver=webdriver.Chrome() ;
        time.sleep(1) ;

        self.log.info("MAZIMIZE THE WINDOW") ;
        driver.maximize_window();
        time.sleep(1) ;

        self.log.info("IMPLICIT WAIT") ;
        driver.implicitly_wait(10);
        time.sleep(1)

        self.log.info("NAVIGATE THE URL") ;
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login") ;
        time.sleep(1) ;

        self.log.info("ENTER THE USERNAME") ;
        driver.find_element(By.XPATH, '//input[@name="username"]').send_keys("Admin") ;
        time.sleep(1) ;

        self.log.info("ENTER THE PASSWORD") ;
        driver.find_element(By.XPATH, '//input[@type="password"]').send_keys("admin123") ;
        time.sleep(1) ;

        self.log.info("CLICK ON THE LOGIN BUTTON") ;
        driver.find_element(By.XPATH, '//button[text()=" Login "]').click() ;
        time.sleep(1) ;

        try:
            self.log.info("LOOKING FOE AN ELEMENT/PAGE TITLE") ;
            driver.find_element(By.XPATH, '//p[@class="oxd-userdropdown-name"]') ;
            time.sleep(1) ;

            self.log.info("TAKING THE SCREENSHOT") ;
            driver.save_screenshot("D:\\PYTHON CT15\\FINAL_REVISION\\screenshots\\test_20_01_ohrm_logs_pass.png") ;

            self.log.info("PRINTING STATEMENT");
            print("***********TEST IS PASSED**********");

            self.log.info("PROCEEDING FOR LOGOUT") ;
            driver.find_element(By.XPATH, '//p[@class="oxd-userdropdown-name"]').click() ;

            driver.find_element(By.XPATH, '//a[contains(text(), "Logout")]').click() ;

            self.log.info("CLOSE THE BROWSER") ;
            driver.close() ;
            assert True ;

        except:
            self.log.info("TAKING THE SCREENSHOT")
            driver.save_screenshot("D:\\PYTHON CT15\\FINAL_REVISION\\screenshots\\test_20_01_ohrm_logs_fail.png") ;

            self.log.info("PRINTING STATEMENT");
            print("***********TEST IS FAILED**********");

            self.log.info("CLOSE THE BROWSER") ;
            driver.close() ;
            assert False ;

        self.log.info("TEST CASE IS COMPLETED") ;
