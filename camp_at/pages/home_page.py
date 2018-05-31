from selenium.webdriver.remote.webdriver import WebDriver

from camp_at.pages.common_elements import PageUrl


class HomePage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def open(self):
        self.driver.get(PageUrl().general_url())

    def check_url(self) -> bool:
        if not self.driver.current_url == PageUrl().general_url():
            return True

        return False


class WhereDoYouWantToGo:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.select_input = self.driver.find_element_by_id('csf_query')
        self.search_dropdown = self.driver.find_element_by_id('countries-search-list')
        self.belgium = self.driver.find_element_by_xpath('//*[@id="countries-search-list"]/li[3]/a')

    def country(self):
        pass

    def country_autocomplete(self):
        self.select_input.click()
        self.belgium.click()

        if 'campsite-select__input valid' not in self.select_input.get_attribute('class'):
            return False

    def region(self):
        self.select_input.click()
        self.select_input.send_keys('Occitania')

        if 'campsite-select__input valid' not in self.select_input.get_attribute('class'):
            return False

    def region_autocomplete(self):
        pass

    def town(self):
        pass

    def town_autocomplete(self):
        pass

    def campsite_name(self):
        pass

    def campsite_name_autocomplete(self):
        pass


class DatePicker:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.check_in = self.driver.find_element_by_id('check_in_side')
        self.check_out = self.driver.find_element_by_id('check-out-select')


class Adults:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.adults_select = self.driver.find_element_by_id('adults-select')

    def number(self):
        pass


class Children:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.children_select = self.driver.find_element_by_id('children-select')
        self.increase_children_btn = self.driver.find_element_by_id('btn-incr-children')
        self.decrease_children_btn = self.driver.find_element_by_id('btn-decr-children')

    def number(self):
        pass

    def age(self):
        pass
