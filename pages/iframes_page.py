from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class IframesPage:

    url = "https://testpages.herokuapp.com/styled/iframes-test.html"

    def __init__(self, browser):
        self.browser = browser

    def load(self):
        self.browser.get(self.url)

    #locators
    iframe_locator = (By.ID, "thedynamichtml")
    frame1_item1_locator = (By.ID, "iframe0")

    def switch_to_iframe(self):
        # Store iframe web element
        iframe = self.browser.find_element(self.iframe_locator)
        # switch to selected iframe
        self.browser.switch_to.frame(iframe)

    def check_iframe_item1(self):
        wait = WebDriverWait(self.browser, 10)
        if wait.until(EC.visibility_of_element_located(self.frame1_item1_locator)):
            return True

    # Now click on button
    # driver.find_element(By.TAG_NAME, 'button').click()