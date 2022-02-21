from pages.window_page import WindowPage

def test_window_example(browser):
    # Background: url required
    # Given url is provided

    # Scenario: automation should be able to open and close windows

    # Given the website is displayed
    window_page = WindowPage(browser)
    window_page.load()
    print(window_page.length_window_handle())
    assert window_page.check_windows_opened(1)
    # When clicking on the new window button
    window_page.open_new_window()
    assert window_page.check_windows_opened(2)
    print(window_page.length_window_handle())
    # And switching focus to the new window
    window_page.open_several_windows(3)
    third_handle = window_page.get_window_handle(3)
    window_page.switch_to_specific_window(third_handle)
    """window_page.switch_to_new_window()"""
    # Then the new window returns it's ID
    # assert window_page.get_window_handle()
