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

    button_locator = (By.XPATH, "//a[contains(text(), 'Click Here')]")

    def open_new_window(self):
        wait = WebDriverWait(self.browser, 120)
        wait.until(EC.visibility_of_element_located(self.button_locator)).click()

    def get_window_handle(self):
        if self.browser.current_window_handle:
            print("Handle is: "+self.browser.current_window_handle+" - .")
            return True
        else:
            return False

    def length_window_handle(self):
        return len(self.browser.window_handles)

    def switch_to_new_window(self):
        """Loops through windows until we find a new window handle. Chrome opens a new tab instead of a new window."""
        original_window = self.browser.current_window_handle  # Handles are randomized codes generated on runtime
        for window_handle in self.browser.window_handles:
            if window_handle != original_window:
                self.browser.switch_to.window(window_handle)
                break

    def close_window(self):
        self.browser.close()

    def check_windows_opened(self, windows: int):
        """Checks whether the specified number of windows is currently open"""
        if len(self.browser.window_handles) == windows:
            return True
        else:
            return False
