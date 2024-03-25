import time

from selenium.webdriver.common.by import By


class Test_orangehrm_pages():
    tf_username=(By.XPATH, '//input[@name="username"]') ;
    tf_password=(By.XPATH, '//input[@name="password"]') ;
    btn_login=(By.XPATH, '//button[text()=" Login "]') ;
    tab_menu=(By.XPATH, '//p[@class="oxd-userdropdown-name"]') ;
    link_logout=(By.XPATH, '//a[contains(text(), "Logout")]') ;

    def __init__(self,driver):
        self.driver=driver ;

    def test_get_url(self,url):
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login") ;
        print("\n*******************STEP1. URL NAVIGATED SUCCESSFULLY****************") ;
        time.sleep(1) ;

    def test_enter_username(self,username):
        self.driver.find_element(*Test_orangehrm_pages.tf_username).send_keys(username);
        print("\n****************STEP2. USERNAME ENTERED SUCCESSFULLY****************")
        time.sleep(1) ;

    def test_enter_password(self,password):
        self.driver.find_element(*Test_orangehrm_pages.tf_password).send_keys(password) ;
        print("\n****************STEP3. PASSWORD ENTERED SUCCESSFULLY****************") ;
        time.sleep(1) ;

    def test_click_login(self):
        self.driver.find_element(*Test_orangehrm_pages.btn_login).click() ;
        print("\n****************STEP4. LOGIN BUTTON CLICKED SUCCESSFULLY****************") ;
        time.sleep(1) ;

    def test_status(self):
        time.sleep(2) ;
        if(self.driver.title=="OrangeHRM"):
            print("\n****************STEP5. LOGIN SUCCESSFULLY****************") ;
            return True;
        else:
            print("\n****************STEP6. LOGIN UNSUCCESSFUL****************") ;
            return False ;

    def test_click_menu_tab(self):
        self.driver.find_element(*Test_orangehrm_pages.tab_menu).click() ;
        print("\n****************STEP6. MENU TAB CLICKED SUCCESSFULLY****************") ;
        time.sleep(1) ;

    def test_click_logout(self):
        self.driver.find_element(*Test_orangehrm_pages.link_logout).click() ;
        print("\n****************STEP7. LOGOUT SUCCESSFULLY****************") ;
        time.sleep(1) ;