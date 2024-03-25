import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from utilities.ReadConfig import ReadConfig

class Test_021_01_orangehrm_conf():

    UserName=ReadConfig.getUserName() ;
    PassWord=ReadConfig.getPassWord() ;

    def test_21_01_hrmo(self):

        driver=webdriver.Chrome() ;
        time.sleep(1) ;

        driver.maximize_window() ;
        time.sleep(1) ;

        driver.implicitly_wait(10) ;

        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login") ;
        time.sleep(1) ;

        driver.find_element(By.XPATH, '//input[@name="username"]').send_keys(self.UserName) ;
        time.sleep(1) ;

        driver.find_element(By.XPATH, '//input[@name="password"]').send_keys(self.PassWord) ;
        time.sleep(1) ;

        driver.find_element(By.XPATH, '//button[contains(text(), "")]').click() ;
        time.sleep(1) ;

        try:
            driver.find_element(By.XPATH, '//p[@class="oxd-userdropdown-name"]') ;

            driver.save_screenshot("D:\\PYTHON CT15\\FINAL_REVISION\\screenshots\\test_021_01_ohrm_cong_pass.png") ;

            print("******************TEST IS PASSED********************") ;

            driver.find_element(By.XPATH, '//p[@class="oxd-userdropdown-name"]').click() ;

            driver.find_element(By.XPATH, '//a[text()="Logout"]').click() ;

            driver.close();
            assert True
        except:

            driver.save_screenshot("D:\\PYTHON CT15\\FINAL_REVISION\\screenshots\\test_021_01_ohrm_cong_fail.png") ;

            print("****************TEST IS FAILED*****************") ;

            driver.close() ;
            assert False ;

