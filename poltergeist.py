# poltergeist

import os
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
        #self.driver = webdriver.Chrome(executable_path="C:\seleniumchromwdriver\chromedriver.exe")
        if os.name == 'nt':
            self.driver = webdriver.Chrome(executable_path="C:\seleniumchromwdriver\chromedriver.exe")
        else:
            self.driver = webdriver.Chrome(executable_path="/opt/chromedriver")
        self.driver.get(self.URL)
        
        try:
            self.finder_field = WebDriverWait (self.driver, 10).until(
                ec.visibility_of_element_located((By.NAME, 'text')))
        except Exception as e:
            print ('self.finder_field failed') 
        
        try:
            self.finder_field.send_keys(self.arg)
        except Exception as e:
            print ('self.finder_field.send_keys failed')

        try:
            self.finder_button = WebDriverWait (self.driver, 10).until(
                ec.visibility_of_element_located((By.NAME, 'search-button')))
        except Exception as e:
            print ('self.finder_button failed')
        try:
            self.finder_button.click()
        except Exception as e:
            print ('self.finder_button.click failed')


        try:
            self.found_list_of_items = WebDriverWait (self.driver, 10).until(
                ec.visibility_of_element_located((By.CLASS_NAME, 'g-i-list-title')))
        except Exception as e:
            print ('found_list_of_items failed')

        try:
            self.first_item = self.found_list_of_items.find_element_by_tag_name('a')
        except Exception as e:
            print ('self.found_list_of_items.find_element_by_tag failed')

        try:
            self.first_item.click()
        except Exception as e:
            print ('self.first_item.click() failed')


if __name__ == '__main__':
    multipad = Article ('Prestigio MultiPad 10.1 3G')
    multipad.FindInRozetka()