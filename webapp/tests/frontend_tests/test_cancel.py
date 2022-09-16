import unittest
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

SLEEP_TIME = 1
CODE = "####-####-####-####"

class CancelTest (unittest.TestCase):

    def setUp(inst):
        #ser = Service('C:\\Program Files (x86)\\chromedriver.exe')
        ser = Service()
        inst.driver = webdriver.Chrome(service=ser)
        inst.driver.implicitly_wait(30)
        inst.driver.maximize_window()
        url = "http://127.0.0.1:8080/"  # Is there a way to boot the instance straight to the cancel appt page?
        inst.driver.get(url)

    def test_cancel_appt(self):
        '''(self) -> None
        Test if interactions to cancel an appointment works.'''
        
        text_code = self.driver.find_element(By.ID, "text_code")
        text_code.send_keys(CODE)
        self.assertEqual(text_code, CODE)
        time.sleep(SLEEP_TIME)

        # If testing "cancel appointment" button is desired:
        # self.driver.find_element(By.ID, "btn_cancel_appt").click()
        # ...