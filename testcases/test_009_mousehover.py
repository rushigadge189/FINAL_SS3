import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


class Test_009_mouse_hover():

    def test_009_mousehover(self):

        driver=webdriver.Chrome() ;
        time.sleep(1) ;

        driver.maximize_window() ;
        time.sleep(1) ;

        driver.implicitly_wait(10) ;

        driver.get('https://www.google.com') ;
        time.sleep(1) ;

        driver.find_element(By.XPATH, '//textarea[@class="gLFyf"]').send_keys('Vtiger') ;
        time.sleep(1) ;

        driver.find_element(By.XPATH, '(//input[@class="gNO89b"])[1]').click() ;
        time.sleep(1) ;

        driver.find_element(By.XPATH, '(//h3[@class="LC20lb MBeuO DKV0Md"])[1]').click() ;
        time.sleep(1) ;

        action=ActionChains(driver) ;

        resource_tab=driver.find_element(By.XPATH, '//a[contains(text(), "Resources")]') ;
        action.move_to_element(resource_tab).perform() ;

        driver.save_screenshot('D:\\PYTHON CT15\\FINAL_REVISION\\screenshots\\test_009_mouse_hoverpass.png') ;

        driver.find_element(By.XPATH, "//div[@class='col-4 p-lg-5']//a[@class='list-link'][normalize-space()='Contact Us']").click() ;
        time.sleep(1) ;

        contact=driver.find_element(By.XPATH, '(//div[@class="text-reset text-decoration-none"])[2]').text ;

        print('\n-----------------CONTACT INFORMATION----------------') ;

        print('\n', contact) ;

        driver.close() ;

