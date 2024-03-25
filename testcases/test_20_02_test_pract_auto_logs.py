from selenium import webdriver
from selenium.webdriver.common.by import By
from utilities.logger import Test_LogGenerator

class Test_20_02_test_pa_logs():

    log=Test_LogGenerator.logger() ;

    def test_20_02_pa_log(self, setup):

        self.log.info("TEST CASE IS STARTED") ;

        self.log.info("OPENING THE BROWSER") ;
        self.driver=setup ;

        self.log.info("NAVIGATING TO THE URL") ;
        self.driver.get("https://practicetestautomation.com/practice-test-login/") ;

        self.log.info("ENTER THE USERNAME") ;
        self.driver.find_element(By.XPATH, '//input[@type="text"]').send_keys('student') ;

        self.log.info("ENTER THE PASSWORD") ;
        self.driver.find_element(By.XPATH, '//input[@type="password"]').send_keys('Password123') ;

        self.log.info("CLICK ON THELOGIN BUTTON") ;
        self.driver.find_element(By.XPATH, '//button[text()="Submit"]').click() ;

        self.log.info("CHECKING FOR THE TITLE/ELEMENT") ;
        if (self.driver.title=="Logged In Successfully | Practice Test Automation") :

            self.log.info("TAKING SCREENSHOT") ;
            self.driver.save_screenshot("D:\\PYTHON CT15\\FINAL_REVISION\\screenshots\\test_20_02_prauto_log_pass.png") ;

            self.log.info("PRINT STATEMENT") ;
            print("***************TEST IS PASSED***************") ;

            self.log.info("PRINTING TEXT AFTER LOGIN") ;
            text1=self.driver.find_element(By.XPATH, '//strong[contains(text(), "Congratulations student. You successfully logged in!")]').text;
            print("**************TEXT AFTER LOGIN*************") ;
            print("\n", text1) ;

            self.log.info("PROCEED FOR LOGOUT") ;
            self.driver.find_element(By.XPATH, '//a[contains(text(), "Log out")]').click() ;

            self.log.info("CLOSING THE BROWSER") ;
            self.driver.close();
            assert True ;

        else:
            self.log.info("TAKING THE SCREENSHOT") ;
            self.driver.save_screenshot("D:\\PYTHON CT15\\FINAL_REVISION\\screenshots\\test_20_02_prauto_log_fail.png") ;

            self.log.info("PRINTTING STATEMENT") ;
            print("****************TEST IS FAILED****************") ;

            self.log.info("CLOSING THE BROWSER") ;
            self.driver.close();
            assert False ;

        self.log.info("TEST IS COMPLETED");