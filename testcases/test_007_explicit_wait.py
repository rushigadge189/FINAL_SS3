import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class Test_007_explicit_waot_demo():

    def test_007_explicit(self):

        driver=webdriver.Chrome();

        driver.maximize_window() ;

        driver.get('https://www.google.com') ;

        driver.find_element(By.XPATH, '//textarea[@jsname="yZiJbe"]').send_keys('Internet Speed Test') ;
        time.sleep(2) ;

        driver.find_element(By.XPATH, '(//input[@value="Google Search"])[1]').click() ;

        driver.find_element(By.XPATH, "//div[contains(text(), 'RUN SPEED TEST')]").click() ;

        try :
            wait=WebDriverWait(driver, 30, poll_frequency=0.5) ;
            wait.until(expected_conditions.visibility_of_element_located((By.XPATH, '(//div[@class="lv7K9c"])[3]'))) ;

            time.sleep(2) ;

            print('-----------------DOWNLOAD SPEED---------------') ;
            download=driver.find_element(By.XPATH, '//div[@class="oyUhj"]').text ;
            print(download) ;

            print('----------------UPLOAD SPEED----------------') ;
            upload=driver.find_element(By.XPATH, '//div[@class="iD3Ij"]').text ;
            print(upload) ;

            driver.save_screenshot("D:\\PYTHON CT15\\FINAL_REVISION\\screenshots\\test_007_explicit_pass.png")

            driver.close();
            assert True ;

        except :

            print('---------------SORRY, SOMETHING WENT WRONG, PLEASE TRY LATER---------------')
            driver.save_screenshot("D:\\PYTHON CT15\\FINAL_REVISION\\screenshots\\test_007_explicit_fail.png") ;
            driver.close() ;

            assert False ;
