from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class WindowPage:

    url = "http://www.learningaboutelectronics.com/Articles/How-to-open-a-new-window-in-Javascript.php"

    def __init__(self, browser):
        self.browser = browser

    def load(self):
        self.browser.get(self.url)

    # locators
    button_locator = (By.XPATH, "//*[@id='para1']/button")

    def open_new_window(self):
        wait = WebDriverWait(self.browser, 10)
        wait.until(EC.visibility_of_element_located(self.button_locator)).click()

    def get_window_handle(self):
        # wait = WebDriverWait(self.browser, 10)
        if self.browser.current_window_handle:
            print("Handle is: "+self.browser.current_window_handle+" - .")
            return True

    def switch_to_new_window(self):
        # Loop through until we find a new window handle
        # original_window = self.browser.current_window_handle()
        # todo here is where the test fails
        self.browser.switch_to.window(1)
        '''for window_handle in self.browser.window_handles:
            if window_handle != original_window:  # todo
                self.browser.switch_to.window(original_window)
                break'''

    def close_window(self):
        self.browser.close()

    def check_windows_opened(self):
        wait = WebDriverWait(self.browser, 10)
        # todo
        return None
