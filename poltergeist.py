# poltergeist

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as ec


class Article():
    """Rozetka Store or Manufacturer Page"""
    def __init__(self, arg):
        self.arg = arg

    def FindInRozetka(self):
        """Find an article at rozetka store"""
        self.URL = 'http://rozetka.com.ua/'
        self.driver = webdriver.Chrome(executable_path="/opt/chromedriver")
        self.driver.get(self.URL)
        
        self.finder_field = WebDriverWait (self.driver, 10).until(
            ec.visibility_of_element_located((By.CLASS_NAME, 'header-search-input-text')))
        
        self.finder_button = WebDriverWait (self.driver, 10).until(
            ec.visibility_of_element_located((By.NAME, 'search-button')))
        
        self.finder_field.send_keys(self.arg)
        self.finder_button.click()


if __name__ == '__main__':
    multipad = Article ('Prestigio MultiPad 10.1 3G')
    multipad.FindInRozetka()