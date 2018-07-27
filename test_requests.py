import unittest
import re
from time import sleep
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as econd
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys

import apiritif

class TestRequests(unittest.TestCase):
    def setUp(self):
        options = webdriver.ChromeOptions()
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10.0)

    def tearDown(self):
        self.driver.quit()

    def test_requests(self):
        self.driver.implicitly_wait(10.0)

        with apiritif.transaction('home'):
            self.driver.get('http://www.blazedemo.com')


        body = self.driver.page_source
        re_pattern = re.compile(r'Welcome tfo the Simple Travel Agency!')
        self.assertNotEqual(0, len(re.findall(re_pattern, body)), "Assertion: 'Welcome to the Simple Travel Agency!' not found in BODY")

        sleep(3.0)

        with apiritif.transaction('ports'):
            self.driver.find_element(By.XPATH, '/html/body/div[3]/form/select[1]/option[6]').click()
            self.driver.find_element(By.XPATH, '/html/body/div[3]/form/select[2]/option[7]').click()
            self.driver.find_element(By.XPATH, '/html/body/div[3]/form/div/input').click()


        sleep(3.0)

