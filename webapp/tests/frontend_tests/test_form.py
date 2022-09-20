import unittest
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

SLEEP_TIME = 1 
NAME = "First Last"
EMAIL = "placeholder@handler.ca"
PHONE = "6134567890"

class FormTest (unittest.TestCase):

    def setUp(inst):
        #ser = Service('C:\\Program Files (x86)\\chromedriver.exe')
        ser = Service()
        inst.driver = webdriver.Chrome(service=ser)
        inst.driver.implicitly_wait(30)
        inst.driver.maximize_window()
        url = "http://127.0.0.1:8080/"  # Is there a way to boot the instance straight to the form page?
        inst.driver.get(url)

    def test_detail_seq(self):
        '''(self) -> None
        Check if the intended sequence of detail inputs works.'''
        # Lots of sleeps, as
            # we intend for the page to update view after each selection,
            # I (Jerry) wanted to simulate users clicking the dropdowns before the options - selenium can "click" the options before they "appear" on screen

        self.driver.find_element(By.ID, "dropdown_doctor").click()
        time.sleep(SLEEP_TIME)
        self.driver.find_element(By.ID, "opt_First_Last").click()
        time.sleep(SLEEP_TIME)

        # TODO: Test calendar interaction here

        self.driver.find_element(By.ID, "dropdown_reason").click()
        time.sleep(SLEEP_TIME)
        self.driver.find_element(By.ID, "opt_checkup").click()
        time.sleep(SLEEP_TIME)

        self.driver.find_element(By.ID, "dropdown_time").click()
        time.sleep(SLEEP_TIME)
        self.driver.find_element(By.ID, "opt_10:00").click()
        time.sleep(SLEEP_TIME)

        # Assuming we go with the one-screen choice for form.
        text_name = self.driver.find_element(By.ID, "text_name")
        text_name.send_keys(NAME)
        self.assertEqual(text_name.text, NAME)
        time.sleep(SLEEP_TIME)
        # If testing submission is also desired, change email to one that can be checked.
        text_email = self.driver.find_element(By.ID, "text_email")
        text_email.send_keys(EMAIL)
        self.assertEqual(text_email.text, EMAIL)
        time.sleep(SLEEP_TIME)

        text_phone = self.driver.find_element(By.ID, "text_phone_number")
        text_phone.send_keys(PHONE)
        self.assertEqual(text_phone.text, PHONE)
        time.sleep(SLEEP_TIME)

        # If testing form submission is also desired:
        # self.driver.find_element(By.ID, "btn_submit").click()

    def test_back_to_home(self):
        '''(self) -> None
        Check if the back-to-home button works.'''

        self.driver.find_element(By.ID, "btn_back_to_home").click()
        self.assertEqual(self.driver.title.lower(), "Book an Appointment".lower())