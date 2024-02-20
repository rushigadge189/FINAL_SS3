import time

from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By


class Test_004_handling_alerts():

    def test_004_alert(self):

        driver=webdriver.Chrome();
        time.sleep(1) ;

        driver.maximize_window() ;
        time.sleep(1) ;

        driver.implicitly_wait(20) ;

        print('\n --------FOR SIMPLE ALERT--------') ;

        driver.get('https://demoqa.com/alerts') ;
        time.sleep(1) ;

        driver.find_element(By.XPATH, '//button[@id="alertButton"]').click() ;
        time.sleep(3) ;

        alert1=Alert(driver).text ;
        print("\n-----------ALERT TEXT-----------") ;
        print("\n",alert1) ;
        print('\n----------------------') ;

        Alert(driver).accept() ;
        time.sleep(1) ;

        print("\n---------ALERT ACCEPTED--------") ;
        driver.close() ;


    def test_004_confirm_alert(self):

        driver=webdriver.Chrome() ;
        time.sleep(1) ;

        driver.maximize_window() ;
        time.sleep(1) ;

        driver.implicitly_wait(20) ;

        print('\n---------FOR CONFIRMATION ALERT---------') ;

        driver.get('https://demoqa.com/alerts') ;
        time.sleep(1) ;

        driver.find_element(By.XPATH, '//button[@id="confirmButton"]').click() ;
        time.sleep(3) ;

        alert2=Alert(driver).text ;
        print('\n----------ALERT TEXT--------') ;
        print('\n', alert2) ;

        Alert(driver).accept() ;
        print('\n---------ALERT ACCEPTED--------') ;

        print('\n-------TEXT AFTER ALERT ACCEPTANCE--------') ;
        alert_res=driver.find_element(By.XPATH, '//span[@id="confirmResult"]').text ;
        print('\n',alert_res) ;
        print('\n----------------------') ;

        driver.find_element(By.XPATH, '//button[@id="confirmButton"]').click() ;
        time.sleep(3) ;

        alert3 = Alert(driver).text;
        print('\n----------ALERT TEXT--------');
        print('\n', alert3);

        Alert(driver).dismiss() ;

        print('\n----------ALERT DISMMISSED----------') ;

        print('\n----------TEXT AFTER ALERT DISSMISSAL---------') ;
        alert_res2=driver.find_element(By.XPATH, '//span[@id="confirmResult"]').text ;
        print('\n' ,alert_res2) ;
        print('\n----------------------');

        driver.close() ;

    def test_004_prompt_alert(self):

        driver=webdriver.Chrome() ;
        time.sleep(1) ;

        driver.maximize_window();
        time.sleep(1) ;

        driver.implicitly_wait(20) ;

        print('\n-------FOR PROMPT ALERT---------') ;

        driver.get('https://demoqa.com/alerts') ;
        time.sleep(5) ;

        driver.find_element(By.XPATH, '(//button[@class="btn btn-primary"])[4]').click() ;
        time.sleep(5) ;

        Alert(driver).send_keys('JAY SHREE RAM........!') ;
        time.sleep(3) ;

        Alert(driver).accept() ;
        time.sleep(1) ;

        print('\n----------TEXT INSERTED-----------') ;

        promt_alert_text=driver.find_element(By.XPATH, '//span[@id="promptResult"]').text ;
        print('\n',promt_alert_text) ;
        print('-----------------') ;

        driver.close() ;







