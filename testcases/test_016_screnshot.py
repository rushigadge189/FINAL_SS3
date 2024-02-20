import time

from selenium import webdriver


class Test_016_scrrenshot():

    def test_016_ss(self):

        driver=webdriver.Chrome() ;
        time.sleep(1) ;

        driver.maximize_window() ;
        time.sleep(1) ;

        driver.implicitly_wait(10) ;

        driver.get( 'https://opensource-demo.orangehrmlive.com/web/index.php/auth/login' ) ;
        time.sleep(1) ;

        if ( driver.title=="OrangeHRM" ) :
            time.sleep(1) ;
            driver.save_screenshot( "D:\\PYTHON CT15\\FINAL_REVISION\\screenshots\\test_016_pass.png" ) ;

            print ( '\n-------------YOU ARE AT HOME PAGE----------------') ;

            driver.close() ;
            assert True;

        else :
            driver.save_screenshot("D:\\PYTHON CT15\\FINAL_REVISION\\screenshots\\test_016_fail.png")
            print( '\n---------------SORRY, YOU ENTERD WRONG URL--------------' ) ;

            driver.close();
            assert True ;

    def test_016_sum(self):

        a=10 ;
        b=20;
        add=a+b;

        if ( add==30 ) :
            print ( "\n-----------------ADDITION IS SUCCESSFUL--------------") ;
            print ( 'RESULT=', add ) ;
            assert True ;

        else:
            print ( 'SORRY, ADDITION IS POSSIBLE' ) ;
            assert False ;


