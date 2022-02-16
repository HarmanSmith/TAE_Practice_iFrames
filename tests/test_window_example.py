from pages.window_page import WindowPage

def test_window_example(browser):
    # Background: url required
    # Given url is provided

    # Scenario: automation should be able to open and close windows

    # Given the website is displayed
    window_page = WindowPage(browser)
    window_page.load()

    # When clicking on the new window button
    window_page.open_new_window()
    # And switching focus to the new window
    window_page.switch_to_new_window()
    # Then the new window returns it's ID
    assert window_page.get_window_handle()
