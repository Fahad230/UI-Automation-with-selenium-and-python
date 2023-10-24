from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import time

class CommonOps:

    def __init__(self,driver):
        self.driver = driver
        self._wait = WebDriverWait(self.driver,20)
        self.longer_wait = WebDriverWait(self.driver,6000)
    
        
    def wait_for(self, locator):
        return self._wait.until(ec.presence_of_element_located(locator))
    
    def wait_for_disappear(self, locator):
        return self.longer_wait.until_not(ec.presence_of_element_located(locator)) 
    
    def wait_for_all(self, locator):
        return self._wait.until(ec.presence_of_all_elements_located(locator))
    
    def find(self, locator):
        return self.driver.find_element(*locator)
    
    def find_all(self, locator):
        time.sleep(3)
        return self.driver.find_elements(*locator)
    
    def scrolldown(self):
        time.sleep(10)
        return self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")

    def scrollup(self):
        time.sleep(10)
        return self.driver.execute_script("scroll(0, 0);")
    
    def pageRefresh(self):
        time.sleep(10)
        return self.driver.refresh()
   
    