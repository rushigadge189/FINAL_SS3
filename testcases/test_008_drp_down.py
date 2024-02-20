import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class Test_008_drpdown() :

    def test_008_drop_down_insurance(self):

        driver=webdriver.Chrome();

        driver.maximize_window() ;

        driver.implicitly_wait(10) ;

        driver.get('https://www.careinsurance.com/rhicl/proposalcp/renew/index-care') ;

        driver.find_element(By.XPATH, '//input[@id="policynumber"]').send_keys('123456789') ;

        driver.find_element(By.XPATH, '//input[@placeholder="DOB"]').click() ;

        month=Select(driver.find_element(By.XPATH, '//select[@class="ui-datepicker-month"]'));
        month.select_by_index(5) ;

        year=Select(driver.find_element(By.XPATH, '//select[@class="ui-datepicker-year"]')) ;
        year.select_by_value('1993') ;

        driver.find_element(By.XPATH, '//a[@data-date="27"]').click() ;

        driver.find_element(By.XPATH, '//input[@placeholder="Contact Number"]').send_keys('7412589630') ;

        driver.save_screenshot('D:\\PYTHON CT15\\FINAL_REVISION\\screenshots\\test_008_dd_pass.png') ;

        driver.close() ;
