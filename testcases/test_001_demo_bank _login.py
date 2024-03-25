import time

from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By


class Test_001_demo_bank_guru_99():

    def test_001_bank_login(self):

        driver=webdriver.Chrome() ;
        time.sleep(1) ;

        driver.maximize_window() ;
        time.sleep(1) ;

        driver.implicitly_wait(5) ;

        driver.get('https://demo.guru99.com/V4/') ;
        time.sleep(1) ;

        driver.find_element(By.XPATH, '//input[@name="uid"]').send_keys('mngr546282') ;
        time.sleep(1) ;

        driver.find_element(By.CSS_SELECTOR, 'input[type="password"]').send_keys('AsYvYne') ;
        time.sleep(1) ;

        driver.find_element(By.NAME, "btnLogin" ).click();
        time.sleep(1) ;

        if (driver.title=='Guru99 Bank Manager HomePage') :
            time.sleep(1) ;
            driver.save_screenshot("D:\\PYTHON CT15\\FINAL_REVISION\\screenshots\\test_001_pass.png") ;

            print('\n--------------CONGRATULATIONS, LOGIN SUCCESSFUL-------------') ;

            driver.find_element(By.XPATH, '//a[text()="Log out"]').click() ;
            time.sleep(1) ;

            Alert(driver).accept();
            time.sleep(1) ;

            driver.close();
            assert True ;

        else:

            driver.save_screenshot("D:\\PYTHON CT15\\FINAL_REVISION\\screenshots\\test_001_fail.png") ;

            print('\n------------SORRY, LOGIN UNSUCCESSFUL-------------') ;

            driver.close() ;
            assert False ;