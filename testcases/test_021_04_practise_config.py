from selenium.webdriver.common.by import By
from utilities.ReadConfig import ReadConfig

class Test_021_04_practise():

    USERNAME=ReadConfig.getUserName() ;
    PASSWORD=ReadConfig.getPassWord() ;

    def test_021_04_practise_test_config(self, setup):

        self.driver=setup ;

        self.driver.get("https://practice.expandtesting.com/login") ;

        self.driver.find_element(By.XPATH, '//input[@name="username"]').send_keys(self.USERNAME) ;

        self.driver.find_element(By.XPATH, '//input[@id="password"]').send_keys(self.PASSWORD) ;

        self.driver.find_element(By.XPATH, '//button[text()="Login"]').click() ;


        try:
            self.driver.find_element(By.XPATH, '//i[contains(text(), " Logout")]') ;

            self.driver.save_screenshot("D:\\PYTHON CT15\\FINAL_REVISION\\screenshots\\test_0021_04_practise_pass.png")

            print("***************TEST IS PASSED************") ;

            text1=self.driver.find_element(By.XPATH, '//h4[@class="subheader"]').text ;
            print("\n", text1) ;

            self.driver.find_element(By.XPATH, '//i[contains(text(), " Logout")]').click() ;

            self.driver.close();
            assert True;

        except:
            self.driver.save_screenshot("D:\\PYTHON CT15\\FINAL_REVISION\\screenshots\\test_0021_04_practise_pass.png")

            print("+****************TEST IS FAILED***************") ;

            self.driver.close() ;
            assert False ;