import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


class Test_mouse_draganddrop():

    def test_012_mouse_dd(self):

        driver=webdriver.Chrome();
        time.sleep(1) ;

        driver.maximize_window();
        time.sleep(1) ;

        driver.implicitly_wait(10) ;

        driver.get('https://demo.automationtesting.in/Static.html') ;
        time.sleep(1) ;


        driver.save_screenshot("D:\\PYTHON CT15\\FINAL_REVISION\\screenshots\\test_012_dd_before.png") ;

        driver.execute_script("window.scrollBy(0,300)") ;
        time.sleep(1) ;

        action=ActionChains(driver) ;

        src=driver.find_element(By.XPATH, '//img[@id="mongo"]') ;
        dest=driver.find_element(By.XPATH, '//div[@id="droparea"]') ;

        action.drag_and_drop(src, dest).perform() ;
        time.sleep(2) ;

        driver.save_screenshot("D:\\PYTHON CT15\\FINAL_REVISION\\screenshots\\test_012_dd_after.png") ;

        driver.close() ;