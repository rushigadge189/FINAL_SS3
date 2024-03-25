import time

from selenium.webdriver.common.by import By


class Test_018_03_practice_test_auto():

    username_tf=(By.XPATH, '//input[@name="username"]') ;
    password_tf=(By.XPATH, '//input[@name="password"]') ;
    login_button=(By.XPATH, '//button[contains(text(), "Submit")]') ;
    element_print=(By.XPATH, '//strong[contains(text(), "Congratulations student. You successfully logged in!")]') ;
    logout_button=(By.XPATH, '//a[text()="Log out"]') ;

    def __init__(self,driver):
        self.driver=driver ;

    def test_get(self,url):
        self.driver.get(url) ;
        time.sleep(1) ;
        print("\n****************STEP1. URL NAVIGATED SUCCESSFULLY**************** ");

    def test_enter_username(self, username):
        self.driver.find_element(*Test_018_03_practice_test_auto.username_tf).send_keys(username) ;
        time.sleep(1) ;
        print("\n****************STEP2. USERNAME ENTERED SUCCESSFULLY**************** ") ;


    def test_enter_password(self, password):
        self.driver.find_element(*Test_018_03_practice_test_auto.password_tf).send_keys(password) ;
        time.sleep(1) ;
        print("\n****************STEP3. PASSWORD ENTERED SUCCESSFULLY****************") ;

    def test_click_login(self):
        self.driver.find_element(*Test_018_03_practice_test_auto.login_button).click() ;
        time.sleep(1) ;
        print("\n****************STEP4. LOGIN BUTTON CLICKED SUCCESSFULLY****************") ;

    def test_status(self):
        if(self.driver.title=="Logged In Successfully | Practice Test Automation"):
            print("\n****************STEP5. LOGIN SUCCESSFUL****************") ;
            return True ;

        else:
            print("\n****************LOGIN UNSUCCESSFUL****************") ;
            print("\n****************STEP5. LOGIN UNSUCCESSFUL****************");
            return False ;

    def test_print(self):
        print123=self.driver.find_element(*Test_018_03_practice_test_auto.element_print).text ;
        print("\n****************TEXT AFTER LOGIN****************") ;
        print("\n", print123) ;
        time.sleep(1) ;
        print("\n****************STEP6. TEXT PRINTED SUCCESSFULLy****************");

    def test_logout(self):
        self.driver.find_element(*Test_018_03_practice_test_auto.logout_button).click() ;
        time.sleep(1) ;
        print("\n****************STEP7. LOGOUT SUCCESSFULLY****************") ;
