import unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

class QaInterviewTest(unittest.TestCase):

    def setUp(self):
        options = Options()
        options.add_argument("start-maximized")
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options )

    def test_qa_selenium_interview(self):
        driver = self.driver
        driver.get("localhost:6464")
        # self.assertIn("factorial", driver.title)
        # heading1 = driver.find_element_by_tag_name('h1')
        number = 5
        # element enter integer number field
        element = driver.find_elements_by_id("number")
        # button factorial
        button = driver.find_elements_by_name("getFactorial")
        # send number
        element.send_keys(number)
        element.send_keys(Keys.RETURN)
        assert "No results found." not in driver.page_source
        button.click()

    # def negative_test_case(self):

    # def empty_test_case(self):


    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main()



