from selenium import webdriver
from selenium.webdriver.common.by import By
from utilities.logger import Test_LogGenerator


class Test_20_03_hero_ku():

    log=Test_LogGenerator.logger() ;

    def test_20_03_log_hk(self,setup):

        self.log.info("TEST IS STARTED") ;

        print("\n*************************************") ;
        print("\n*********LOG LEVEL EXAMPLE**********") ;
        self.log.debug("\n*****THIS IS THE DEBUG LOG*****") ;
        self.log.info("\n*****THIS IS THE INFO LOG*****") ;
        self.log.warning("\n*****THIS IS THE WARNING LOG*****") ;
        self.log.error("\n*****THIS IS THE ERROR LOG*****") ;
        self.log.critical("\n*****THIS IS THE CRITICAL LOG*****") ;

        print("\n***********************************");

        self.log.info("OPENING THE BROWSER") ;

        self.log.info("MAXIMIZE THE WINDOW") ;

        self.driver=setup ;


        self.log.info("NAVIGATING TO THE URL") ;
        self.driver.get("https://the-internet.herokuapp.com/login") ;

        self.log.info("ENTERING THE USERNAME") ;
        self.driver.find_element(By.XPATH, '//input[@name="username"]').send_keys('tomsmith') ;

        self.log.info("ENTER THE PASSWORD") ;
        self.driver.find_element(By.XPATH, '//input[@type="password"]').send_keys('SuperSecretPassword!') ;

        self.log.info("CLICK ON THE LOGIN BUTTON") ;
        self.driver.find_element(By.XPATH, '//button[@type="submit"]').click() ;

        try :
            self.log.info("CHECK FOR THE PAGE TITLE/ELEMENT") ;
            self.driver.find_element(By.XPATH, '//i[@class="icon-2x icon-signout"]') ;

            self.log.info("TAKING THE SCREENSHOT") ;
            self.driver.save_screenshot("D:\\PYTHON CT15\\FINAL_REVISION\\screenshots\\test_20_03_heroku_pass.png") ;

            self.log.info("PRINTING STATEMENT") ;
            print("******************TEST IS PASSED***************") ;

            self.log.info("TEXT AFTER LOGIN") ;
            print("****************TEXT AFTER LOGIN****************") ;

            text1=self.driver.find_element(By.XPATH, '//h4[@class="subheader"]').text ;
            print("\n", text1) ;

            self.log.info("PROCEEDING FOR LOGOUT") ;
            self.driver.find_element(By.XPATH, '//i[@class="icon-2x icon-signout"]').click() ;

            self.log.info("CLOSING THE BROWSER") ;
            self.driver.close();
            assert True ;

        except :

            self.log.info("TAKING THE SCREENSHOT") ;
            self.driver.save_screenshot("D:\\PYTHON CT15\\FINAL_REVISION\\screenshots\\test_20_03_heroku_fail.png");

            self.log.info("PRINTING STATEMENT") ;
            print("**************TEST IS FAILED**************") ;

            self.log.info("CLOSING THE BROWSER") ;
            self.driver.close() ;
            assert False ;

        self.log.info("TEST IS COMPLETED");