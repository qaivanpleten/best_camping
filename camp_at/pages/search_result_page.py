from selenium.webdriver.remote.webdriver import WebDriver


class SearchResultPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def check_page_title(self, country) -> bool:
        title = self.driver.find_element_by_xpath('/html/head/meta[2]')
        if 'Results for “' + country + '”' not in title.get_attribute('content'):
            return False

        return True
