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

    iframe_locator = "thedynamichtml"  # Iframe locators are always found by ID that's why the locator is a string
    frame1_item1_locator = (By.ID, "iframe0")

    def switch_to_iframe(self):
        self.browser.switch_to.frame(self.iframe_locator)

    def check_iframe_item1(self):
        wait = WebDriverWait(self.browser, 10)
        return wait.until(EC.visibility_of_element_located(self.frame1_item1_locator))
