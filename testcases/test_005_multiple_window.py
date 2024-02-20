import encodings.punycode
import time

from selenium import webdriver
from selenium.webdriver.common.by import By


class Test_005_multiple_window_handle() :

    def test_005_handle_multiple_windows(self):

        driver=webdriver.Chrome() ;
        time.sleep(1) ;

        driver.maximize_window() ;
        time.sleep(1) ;

        driver.implicitly_wait(10) ;

        driver.get('https://the-internet.herokuapp.com/windows') ;
        time.sleep(1) ;

        driver.find_element(By.XPATH, '//a[text()="Click Here"]').click() ;
        time.sleep(1) ;

        allwindow=driver.window_handles ;
        time.sleep(1) ;

        driver.switch_to.window(allwindow[1]) ;
        print("\n---------TEXT IN CHILD WINDOW--------")
        text1=driver.find_element(By.XPATH, '//h3[text()="New Window"]').text ;
        print('\n', text1) ;
        driver.save_screenshot("D:\PYTHON CT15\FINAL_REVISION\screenshots\\test_005_child.png") ;
        time.sleep(1) ;

        driver.switch_to.window(allwindow[0]) ;
        text2=driver.find_element(By.XPATH, '//h3[text()="Opening a new window"]').text ;
        print('\n--------TEXT IN PARRENT WINDOW---------') ;
        print('\n', text2) ;
        driver.save_screenshot('D:\\PYTHON CT15\\FINAL_REVISION\\screenshots\\test_005_parent.png') ;


        driver.close() ;