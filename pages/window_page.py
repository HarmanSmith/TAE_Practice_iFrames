from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class WindowPage:

    url = "https://the-internet.herokuapp.com/windows"

    def __init__(self, browser):
        self.browser = browser

    def load(self):
        self.browser.get(self.url)

    # locators
    button_locator = (By.XPATH, "//a[contains(text(), 'Click Here')]")
    # //*[@id="content"]/div/a

    def open_new_window(self):
        wait = WebDriverWait(self.browser, 120)
        wait.until(EC.visibility_of_element_located(self.button_locator)).click()
        # wait.until(EC.number_of_windows_to_be(2))
        # number_of_windows includes number of tabs?

    def get_window_handle(self):
        # wait = WebDriverWait(self.browser, 10)
        if self.browser.current_window_handle:
            print("Handle is: "+self.browser.current_window_handle+" - .")
            return True
        else:
            return False

    def length_window_handle(self):
        return len(self.browser.window_handles)

    def switch_to_new_window(self):
        # Loop through until we find a new window handle
        # chrome opens a new tab instead of a new window
        # fixed by obtaining the long window handle for each session
        original_window = self.browser.current_window_handle
        for window_handle in self.browser.window_handles:
            if window_handle != original_window:
                self.browser.switch_to.window(window_handle)
                break

    def close_window(self):
        self.browser.close()

    def check_windows_opened(self, index):
        # wait = WebDriverWait(self.browser, 10)
        if len(self.browser.window_handles) == index:
            return True
        else:
            return False
