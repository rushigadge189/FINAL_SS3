import time

from selenium.webdriver.common.by import By


class Test_swaglabspages():

    username_tf=(By.XPATH, '//input[@placeholder="Username"]') ;
    password_tf=(By.XPATH, '//input[@placeholder="Password"]') ;
    login_btn=(By.XPATH, '//input[@name="login-button"]') ;
    hamburger_icon=(By.XPATH, '//button[@id="react-burger-menu-btn"]') ;
    logout_link=(By.XPATH, '//a[text()="Logout"]') ;

    def __init__(self,driver):
        self.driver=driver ;

    def test_get_url(self,url):
        self.driver.get(url) ;
        time.sleep(1) ;
        print("\n********STEP1. URL NAVIGATED SUCCESSFULLY*********") ;

    def test_enter_username(self, username):
        self.driver.find_element(*Test_swaglabspages.username_tf).send_keys(username) ;
        time.sleep(1) ;
        print("\n*********STEP2. USERNAME ENTERED SUCCESSFULLY*********") ;

    def test_enter_pasword(self, password):
        self.driver.find_element(*Test_swaglabspages.password_tf).send_keys(password) ;
        time.sleep(1) ;
        print("\n*********STEP3. PASSWORD ENTERED SUCCESSFULLY*********") ;

    def test_click_login(self):
        self.driver.find_element(*Test_swaglabspages.login_btn).click();
        time.sleep(1) ;
        print("\n*********STEP4. LOGIN BUTTON CLICKED*********") ;

    def test_status(self):
        if(self.driver.title=="Swag Labs") :
            print("\n*********STEP5. LOGIN SUCCESSFULLY*********") ;
            return True ;

        else:
            print("\n*********STEP5. LOGIN UNSUCCESSFUL*********") ;
            return False ;

    def test_ham_bur_icon_click(self):
        self.driver.find_element(*Test_swaglabspages.hamburger_icon).click() ;
        time.sleep(1) ;
        print("\n*********STEP6. HAMBURGER ICON CLICKED SUCCESSFULLY*********") ;

    def test_logout_click(self):
        self.driver.find_element(*Test_swaglabspages.logout_link).click();
        time.sleep(1) ;
        print("\n*********STEP7. LOGOUT SUCCESSFULLY*********") ;

