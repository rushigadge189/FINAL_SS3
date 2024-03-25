from selenium import webdriver
from selenium.webdriver.common.by import By
from utilities.logger import Test_LogGenerator

class Test_20_04_pracctice():

    log=Test_LogGenerator.logger() ;

    def test_20_04_practice_auto_log(self):

        self.log.info("TEST IS STARTED") ;

        self.log.info("OPENING THE BROWSER") ;
        driver=webdriver.Chrome() ;

        self.log.info("MAXIMIZE THE WINDOW") ;
        driver.maximize_window() ;

        driver.implicitly_wait(10) ;

        self.log.info("NAVIGATE TO THE URL") ;
        driver.get("https://practice.expandtesting.com/login") ;

        self.log.info("ENTER THE USERNAME") ;
        driver.find_element(By.XPATH, '//input[@name="username"]').send_keys('practice') ;

        self.log.info("ENTER THE PASSWORD") ;
        driver.find_element(By.XPATH, '//input[@name="password"]').send_keys('SuperSecretPassword!') ;

        self.log.info("CLICK ON THE LOGIN BUTTON") ;
        driver.find_element(By.XPATH, '//button[@type="submit"]').click() ;

        self.log.info("CHECKING FOR THE TITLE") ;
        if(driver.title=="Test Automation Practice: Working with Secure Page") :

            self.log.info("TAKING THE SCREENSHOT") ;
            driver.save_screenshot("D:\\PYTHON CT15\\FINAL_REVISION\\screenshots\\practice_logs_pass.png") ;

            self.log.info("PRINTING STATUS") ;
            print("\n******************TEST IS PASSED****************") ;

            self.log.info("PRINT TEXT AFTER LOGIN") ;
            text1=driver.find_element(By.XPATH, '//h4[@class="subheader"]').text ;
            print("***************TEXT AFTER LOGIN****************") ;
            print("\n", text1) ;

            self.log.info("LOGOUT FROM THE APPLICATION") ;
            driver.find_element(By.XPATH, '//i[contains(text(), " Logout")]').click() ;

            self.log.info("CLOSE THE BROWSER") ;
            driver.close() ;
            assert True ;

        else:

            self.log.info("TAKING THE SCREENSHOT") ;
            driver.save_screenshot("D:\\PYTHON CT15\\FINAL_REVISION\\screenshots\\practice_logs_fail.png");

            self.log.info("PRINTING STATUS") ;
            print("\n******************TEST IS FAILED****************");

            self.log.info("CLOSING THE BROWSER") ;
            driver.close();
            assert False ;

        self.log.info("TEST IS COMPLETED");