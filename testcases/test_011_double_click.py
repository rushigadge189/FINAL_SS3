import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By


class Test_011_double_click():

    def test_011_mouse_double_click(self):

        driver=webdriver.Chrome() ;
        time.sleep(1);

        driver.maximize_window();
        time.sleep(1) ;

        driver.implicitly_wait(1) ;

        driver.get('https://demo.guru99.com/test/simple_context_menu.html') ;
        time.sleep(1) ;

        action=ActionChains(driver) ;
        double_click=driver.find_element(By.XPATH, '//button[@ondblclick="myFunction()"]') ;

        action.double_click(double_click).perform() ;
        time.sleep(1) ;

        print('\n-----------------ALERT TEXT AFTER DOUBLE CLICK----------------') ;
        text1=Alert(driver).text ;
        print('\n', text1) ;

        Alert(driver).accept();
        time.sleep(1) ;

        driver.close() ;