from selenium.webdriver.common.by import By
import time
from .common_ops import CommonOps


class LoginPage(CommonOps):
    login_username = (By.XPATH,'//input[@placeholder="Please enter your Phone Number or Email"]')
    login_password = (By.XPATH,'//input[@placeholder="Please enter your password"]')
    login_button = (By.XPATH,'//button[@type="submit"]')

    def enter_login_username(self,username):
        self.wait_for(self.login_username).send_keys(username)  

    def enter_login_password(self,password):
        self.find(self.login_password).send_keys(password)
    
    def click_login_submit_button(self):
        self.find(self.login_button).click()
