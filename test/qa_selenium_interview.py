import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

class QaInterviewTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())

    def test_qa_selenium_interview(self):
        driver = self.driver
        driver.get("localhost:6464")
        # self.assertIn("factorial", driver.title)
        
        heading1 = driver.find_element_by_tag_name('h1')
        
        number = 5
        element = driver.find_elements_by_name(self, "number")
        button = driver.find_elements_by_id(self, "getFactorial")
        element.send_keys(number)
        element.send_keys(Keys.RETURN)
        assert "No results found." not in driver.page_source
        button.click()

        def negative_test_case():


        def nu

    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main()



