import time

from selenium.webdriver.common.by import By


class Test_018_04_herko_pages():

    username_tf=(By.XPATH, '//input[@name="username"]')
    password_tf=(By.XPATH, '//input[@name="password"]')
    login_button=(By.XPATH, "//i[contains(text(),' Login')]")
    print_text=(By.XPATH, '//h4[@class="subheader"]') ;
    logout_button=(By.XPATH, '//i[text()=" Logout"]') ;

    def __init__(self,driver):
        self.driver=driver ;


    def test_get_url(self,url):
        self.driver.get(url) ;
        print('\n*************STEP1. URL NAVIGATED SUCCESSFULLY*************') ;
        time.sleep(1) ;

    def test_enter_username(self, username):
        self.driver.find_element(*Test_018_04_herko_pages.username_tf).send_keys(username) ;
        print('\n*************STEP2. USERNAME ENTERED SUCCESSFULLY*************') ;
        time.sleep(1) ;

    def test_enter_password(self, password):
        self.driver.find_element(*Test_018_04_herko_pages.password_tf).send_keys(password) ;
        print('\n*************STEP3. PASSWORD ENTERED SUCCESSFULLY*************') ;
        time.sleep(1) ;

    def test_login(self):
        self.driver.find_element(*Test_018_04_herko_pages.login_button).click() ;
        print('\n*************STEP4. LOGIN BUTTON CLICKED SUCCESSFULLY*************') ;
        time.sleep(1) ;

    def test_status(self):
        if(self.driver.title=='The Internet') :
            print('\n*************STEP5. LOGIN SUCESSFULLY*************') ;
            time.sleep(1) ;
            return True ;


        else:
            print('\n*************STEP5. LOGIN UNSUCESSFUL*************') ;
            time.sleep(1) ;
            return False ;

    def test_print_text_after_login(self):
        print1=self.driver.find_element(*Test_018_04_herko_pages.print_text).text ;
        print('\n*************TEXT AFTER LOGIN*************') ;
        print('\n', print1) ;
        print("\n*************STEP6. TEXT AFTER LOGIN PRINTED SUCCESSFULLY*************") ;
        time.sleep(1) ;

    def test_logout(self):
        self.driver.find_element(*Test_018_04_herko_pages.logout_button).click() ;
        print("\n*************STEP7. LOGOUT SUCCESSFULLY*************") ;
        time.sleep(1) ;
