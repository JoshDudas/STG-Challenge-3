import unittest
import selenium
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait


class AutomatedChromeBrowser (unittest.TestCase):

    def setUp(self):
        self.driver = selenium.webdriver.Chrome('./chromedriver')

    def test_getandListPopularItems(self):
        self.driver.get('https://www.copart.com')

        driver_wait = WebDriverWait(self.driver, 30)
        driver_wait.until(expected_conditions.presence_of_element_located((By.XPATH, "//a[contains(@href, './popular/make/')]")))

        popular_makes_models = self.driver.find_elements(By.XPATH, "//a[contains(@href, './popular/make/')]")
        popular_makes_models += self.driver.find_elements(By.XPATH, "//a[contains(@href, './popular/model/')]")

        popular_makes_models_count = len(popular_makes_models)

        i = 0
        while i < popular_makes_models_count:
            print(str(popular_makes_models[i].text) + " - " + str(popular_makes_models[i].get_attribute('href')))
            i += 1

        for make_model in popular_makes_models:
            print(str(make_model.text) + ' - ' + str(make_model.get_attribute('href')))

    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main()


