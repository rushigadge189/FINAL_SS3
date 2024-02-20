import time

from selenium import webdriver
from selenium.webdriver.common.by import By


class Test_006_implicitwait() :

    def test_006_implicit_wait_demo(self):

        driver=webdriver.Chrome() ;
        time.sleep(1) ;

        driver.maximize_window() ;
        time.sleep(1) ;

        driver.implicitly_wait(25) ;

        driver.get('https://www.google.com') ;
        time.sleep(1) ;

        driver.find_element(By.XPATH ,'//textarea[@jsaction="paste:puy29d;"]').send_keys('Internet Speed Test') ;
        time.sleep(2) ;

        driver.find_element(By.XPATH, '(//input[@value="Google Search"])[1]').click() ;
        time.sleep(1) ;

        driver.find_element(By.XPATH, '//div[text()="RUN SPEED TEST"]').click() ;
        time.sleep(25) ;

        print("\n-------------------DOWNLOAD SPEED-----------------") ;
        download=driver.find_element(By.XPATH, '//div[@class="oyUhj"]').text ;
        print(download) ;

        print("\n------------------UPLOAD SPEED-------------------")
        upload=driver.find_element(By.XPATH, '//div[@class="iD3Ij"]').text ;
        print(upload) ;

        driver.save_screenshot('D:\\PYTHON CT15\\FINAL_REVISION\\screenshots\\test_006_implicit_pass.png') ;

        driver.close() ;







