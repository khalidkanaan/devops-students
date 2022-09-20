import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

#This set of tests is for the front-end functionality of the Pre-screening page, specifically, filling out the quiz and redirecting to the Booking page.
class HomepageTest(unittest.TestCase):

    def setUp(inst):
        #ser = Service('C:\\Program Files (x86)\\chromedriver.exe')
        ser = Service()
        inst.driver = webdriver.Chrome(service=ser)
        inst.driver.implicitly_wait(10) #driver has 10s to find element when page first loads
        inst.driver.maximize_window()
        url = "http://127.0.0.1:5000/"
        inst.driver.get(url)

    def test_pass_prescreening(self):
        self.driver.find_element(By.ID, "booknow").click() #press button

        self.driver.find_element(By.ID, "next").click() #goto next form

        #click no for "close contact"
        self.driver.find_element(By.ID, "cc_no").click()
        #click no for "travelled"
        self.driver.find_element(By.ID, "tr_no").click()
        self.driver.find_element(By.ID, "next").click() #goto next form

        self.driver.find_element(By.ID, "tested_no").click()
        self.driver.find_element(By.ID, "submit").click()

        #check if next page is booking page
        title = self.driver.title
        self.assertEqual(title.lower(),"Booking".lower()) #<title> of page


    def test_fail_prescreening(self):
        self.driver.find_element(By.ID, "booknow").click() #press button

        self.driver.find_element(By.ID, "sym3").click() #press checkbox
        self.driver.find_element(By.ID, "next").click() #goto next form

        #click yes for "close contact"
        self.driver.find_element(By.ID, "cc_yes").click()
        #click no for "travelled"
        self.driver.find_element(By.ID, "tr_no").click()
        self.driver.find_element(By.ID, "next").click() #goto next form

        self.driver.find_element(By.ID, "tested_no").click()
        self.driver.find_element(By.ID, "submit").click()

        #check if next page is booking page
        title = self.driver.title
        self.assertEqual(title.lower(),"Booking".lower()) #<title> of page


    def tearDown(inst):
        inst.driver.quit()

if __name__ == "__main__":
    unittest.main()