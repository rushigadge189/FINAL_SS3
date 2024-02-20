import time

from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By


class Test_003_add_customer_guru():

    def test_003_new_cust(self):

        driver=webdriver.Chrome();
        time.sleep(1) ;

        driver.maximize_window();
        time.sleep(1) ;

        driver.implicitly_wait(5) ;

        driver.get('https://demo.guru99.com/V4/index.php') ;
        time.sleep(1) ;

        driver.find_element(By.NAME, "uid").send_keys('mngr546282') ;
        time.sleep(1) ;

        driver.find_element(By.XPATH, '//input[@type="password"]').send_keys('AsyvYne') ;
        time.sleep(1) ;

        driver.find_element(By.XPATH, '//input[@value="LOGIN"]').click() ;
        time.sleep(1) ;

        if(driver.title== 'Guru99 Bank Manager HomePage') :
            driver.save_screenshot('D:\\PYTHON CT15\\FINAL_REVISION\\screenshots\\test_003_login_pass.png') ;

            print('---------LOGIN SUCCESSFUL-------') ;

            driver.find_element(By.XPATH, '//a[text()="New Customer"]').click() ;
            time.sleep(1) ;

            driver.find_element(By.NAME, 'name').send_keys('Sonali Abhishek Shinde') ;
            time.sleep(1) ;

            driver.find_element(By.CSS_SELECTOR, 'input[value="f"]').click() ;
            time.sleep(1) ;

            driver.find_element(By.ID, 'dob').send_keys('24011993') ;
            time.sleep(1) ;

            driver.find_element(By.XPATH, '//textarea[@onkeyup="validateAddress();"]').send_keys('M G Road LBS Palace') ;
            time.sleep(1) ;

            driver.find_element(By.XPATH, '//input[@name="city"]').send_keys('Pune') ;
            time.sleep(1);

            driver.find_element(By.XPATH, '//input[@name="state"]').send_keys('Maharashtra') ;
            time.sleep(1) ;

            driver.find_element(By.XPATH, '//input[@name="pinno"]').send_keys('123456') ;
            time.sleep(1) ;

            driver.find_element(By.XPATH, '//input[@name="telephoneno"]').send_keys('1234567890') ;
            time.sleep(1) ;

            driver.find_element(By.XPATH, '//input[@name="emailid"]').send_keys('abcdefg123456@gmail.com') ;
            time.sleep(1) ;

            driver.find_element(By.XPATH, '//input[@name="password"]').send_keys('abcdefg123456') ;
            time.sleep(1) ;

            driver.find_element(By.XPATH, '//input[@value="Submit"]').click() ;
            time.sleep(5) ;

            print("\n---------CUSTOMER ADDED SUCCESSFULLy--------") ;

            driver.save_screenshot('D:\\PYTHON CT15\\FINAL_REVISION\\screenshots\\test_003_new_cust.png') ;
            time.sleep(1) ;

            driver.find_element(By.XPATH, '//a[text()="Continue"]').click() ;
            time.sleep(1) ;

            driver.find_element(By.XPATH, '//a[text()="Log out"]').click() ;
            time.sleep(1) ;

            Alert(driver).accept();
            time.sleep(1) ;

            driver.close();
            assert True ;

        else:
            driver.save_screenshot('D:\\PYTHON CT15\\FINAL_REVISION\\screenshots\\test_003_login_fail.png');

            print('---------SORRY, LOGIN UNSUCCESSFUL-------');

            driver.close();
            assert False ;
