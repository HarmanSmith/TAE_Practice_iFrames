from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class IframesPage:

    url = "http://www.learningaboutelectronics.com/Articles/How-to-open-a-new-window-in-Javascript.php"

    def __init__(self, browser):
        self.browser = browser

    def load(self):
        self.browser.get(self.url)

    # locators
    button_locator = (By.XPATH, "//*[@id='para1']/button")

    def click_new_window(self):
        wait = WebDriverWait(self.browser, 10)
        wait.until(EC.visibility_of_element_located(self.button_locator)).click()

    def get_window_handle(self):
        return self.browser.current_window_handle

    def check_windows_opened(self):
        wait = WebDriverWait(self.browser, 10)
        return None

    def switch_to_window_index(self, index):
        return None
