import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class Test_008_facebook_dd():

    def test_008_fb(self):

        driver=webdriver.Chrome();
        time.sleep(1) ;

        driver.maximize_window();
        time.sleep(1);

        driver.implicitly_wait(10) ;

        driver.get('https://www.facebook.com') ;
        time.sleep(1);

        driver.find_element(By.XPATH, '//a[@class="_42ft _4jy0 _6lti _4jy6 _4jy2 selected _51sy"]').click() ;
        time.sleep(1);

        driver.find_element(By.XPATH, '//input[@placeholder="First name"]').send_keys('Tushar') ;
        time.sleep(1);

        driver.find_element(By.XPATH, '(//input[@class="inputtext _58mg _5dba _2ph-"])[2]').send_keys('Kathalkar') ;
        time.sleep(1);

        driver.find_element(By.XPATH, '//input[@aria-label="Mobile number or email address"]').send_keys('1234567890') ;
        time.sleep(1);

        driver.find_element(By.XPATH, '//input[@id="password_step_input"]').send_keys('@#abc@123') ;
        time.sleep(1);

        day=Select(driver.find_element(By.XPATH, '//select[@name="birthday_day"]'));
        day.select_by_index(25) ;
        time.sleep(1);

        month=Select(driver.find_element(By.XPATH, '//select[@id="month"]')) ;
        month.select_by_visible_text('Jun') ;
        time.sleep(1);

        year=Select(driver.find_element(By.XPATH, '//select[@title="Year"]')) ;
        year.select_by_value('1993') ;
        time.sleep(1);

        driver.find_element(By.XPATH, '(//input[@type="radio"])[1]').click();
        time.sleep(1);

        driver.save_screenshot('D:\\PYTHON CT15\\FINAL_REVISION\\screenshots\\test_008_fbdd_pass.png') ;

        driver.close() ;