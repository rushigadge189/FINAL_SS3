from selenium.webdriver.common.by import By

from utilities import XUTils

class Test_019_04_heroku():

    def test_019_04_heroku_ddt(self, setup):

        self.driver=setup ;
        
        path="D:\\PYTHON CT15\\FINAL_REVISION\\testdata\\HEROKU_LOGIN.xlsx" ;

        rows=XUTils.rowCount(path, 'Sheet1') ;

        for r in range (2, rows+1) :

            self.driver.get('https://the-internet.herokuapp.com/login') ;

            username=XUTils.readData(path, 'Sheet1', r, 1) ;
            password=XUTils.readData(path, 'Sheet1', r, 2) ;

            self.driver.find_element(By.XPATH, '//input[@id="username"]').send_keys(username) ;

            self.driver.find_element(By.XPATH, '//input[@id="password"]').send_keys(password) ;

            self.driver.find_element(By.XPATH, '//i[contains(text(), " Login")]').click() ;

            try:

                self.driver.find_element(By.XPATH, '//i[@class="icon-2x icon-signout"]') ;

                print("\n*************TEST IS PASSED**************") ;

                self.driver.save_screenshot('D:\\PYTHON CT15\\FINAL_REVISION\\screenshots\\test_019_04_heroku_pass.png') ;

                XUTils.writeData(path, 'Sheet1', r, 3, "PASSED") ;

                print1=self.driver.find_element(By.XPATH, '//h4[@class="subheader"]').text ;
                print("\n***************TEXT AFTER LOGIN*************") ;
                print("\n",print1) ;

                self.driver.find_element(By.XPATH, '//i[@class="icon-2x icon-signout"]').click() ;

            except:
                self.driver.save_screenshot('D:\\PYTHON CT15\\FINAL_REVISION\\screenshots\\test_019_04_heroku_fail.png') ;

                print("\n**************TEST IS FAILED*************") ;

                XUTils.writeData(path, 'Sheet1', r, 3, 'FAILED') ;

        self.driver.close() ;