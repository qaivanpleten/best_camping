import time

from selenium.webdriver.remote.webdriver import WebDriver

from camp_at.pages.common_elements import PageUrl


class HomePage:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        #self.find_campsite_button = self.driver.find_element_by_xpath('//*[@id="search_form"]/div[3]/button')

    def open(self):
        self.driver.get(PageUrl().general_url())

    def check_url(self) -> bool:
        if not self.driver.current_url == PageUrl().general_url():
            return True

        return False

    def perform_search(self):
        #self.find_campsite_button.click()
        self.driver.find_element_by_xpath('//*[@id="search_form"]/div[3]/button').click()


class WhereDoYouWantToGo:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.select_input = self.driver.find_element_by_id('csf_query')
        self.search_dropdown = self.driver.find_element_by_id('countries-search-list')
        self.belgium = self.driver.find_element_by_xpath('//*[@id="countries-search-list"]/li[3]/a')

    def country(self):
        pass

    def select_country_autocomplete(self):
        self.select_input.click()
        self.belgium.click()

    def set_region(self):
        self.select_input.click()
        self.select_input.send_keys('Occitania')

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

    def location_is_set(self):
        if 'campsite-select__input valid' not in self.select_input.get_attribute('class'):
            return False

        return True


class DatePicker:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.check_in = self.driver.find_element_by_id('check-in-select')
        self.check_out = self.driver.find_element_by_id('check-out-select')

    def set_the_date(self):
        self.check_in.click()
        self.driver.find_element_by_xpath('/html/body/div[10]/div[2]/div[1]/table/tbody/tr[3]/td[2]').click()
        time.sleep(2)
        self.driver.find_element_by_xpath('/html/body/div[10]/div[2]/div[1]/table/tbody/tr[3]/td[6]').click()


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

    def set_number(self):
        self.children_select.click()
        self.increase_children_btn.click()
        time.sleep(1)
        # open age dropdown
        self.driver.find_element_by_xpath('//*[@id="children-select"]/div[3]/div[2]/div[2]/div[2]/div/div/div[1]/div/div').click()
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="children-select"]/div[3]/div[2]/div[2]/div[2]/div/div/div[2]/ul/li[3]').click()






    def age(self):
        pass
