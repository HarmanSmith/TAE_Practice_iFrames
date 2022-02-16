from pages.iframes_page import IframesPage


def test_iframe_example(browser):
    # Background: url required
    # Given url is provided

    # Scenario: iFrames should load properly

    # Given the website is displayed
    iframes_page = IframesPage(browser)
    iframes_page.load()

    # When checking the content inside the iFrames
    iframes_page.switch_to_iframe()
    # Then the iFrames work as expected
    assert iframes_page.check_iframe_item1()
