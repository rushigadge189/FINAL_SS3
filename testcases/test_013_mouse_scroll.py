import time

from selenium import webdriver


class Test_013_mousescroll():

    def test_013_scroll(self):

        driver=webdriver.Chrome();

        driver.maximize_window();

        driver.implicitly_wait(10) ;

        driver.get('https://www.bbc.com/') ;

        driver.save_screenshot('D:\\PYTHON CT15\\FINAL_REVISION\\screenshots\\test_013_before_scroll.png') ;
        time.sleep(2) ;

        driver.execute_script("window.scrollBy(0,1000)") ;

        driver.save_screenshot('D:\\PYTHON CT15\\FINAL_REVISION\\screenshots\\test_013_after_scroll.png');
        time.sleep(2) ;

        driver.close() ;
