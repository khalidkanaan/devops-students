import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

#This set of tests is for the front-end functionality of the Homepage, specifically, redirection to the appropriate pages.
class HomepageTest(unittest.TestCase):

    def setUp(inst):
        #ser = Service('C:\\Program Files (x86)\\chromedriver.exe')
        ser = Service()
        inst.driver = webdriver.Chrome(service=ser)
        inst.driver.implicitly_wait(10)
        inst.driver.maximize_window()
        url = "http://127.0.0.1:5000/"
        inst.driver.get(url)

    def test_booknow_redirect(self):
        #check if 'Book now' button redirects to Prescreening.html

        self.driver.find_element(By.ID, "booknow").click() #press button
        title = self.driver.title
        self.assertEqual(title.lower(),"COVID-19 Pre-screening".lower()) #<title> of page

    def test_admin_login(self):
        username = "admin"
        password = "admin"

        #check if 'Admin login' button redirects to Login.html then dashboard.html
        #on successful login

        self.driver.find_element(By.ID, "login").click() #press button
        title = self.driver.title
        self.assertEqual(title.lower(),"Admin Login".lower()) #<title> of page

        #enter username & password, click submit
        driver.find_element(By.ID, "user_id").send_keys(username)
        driver.find_element(By.ID, "password").send_keys(password)
        driver.find_element(By.ID, "submit").click() #press 'Login'

        title = self.driver.title
        self.assertEqual(title.lower(),"Admin Dashboard".lower()) #<title> of page

    def tearDown(inst):
        inst.driver.quit()

if __name__ == "__main__":
    unittest.main()