from selenium.webdriver.remote.webdriver import WebDriver


class PageUrl:
    def general_url(self):
        url = "https://www.campsited.com/"
        return url


class Navbar:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.logo = self.driver.find_element_by_xpath('//*[@id="header"]/div/div[1]/div/a/img')
        self.wish_list_button = self.driver.find_element_by_xpath('//*[@id="header"]/div/div[1]/ul/li[1]/a')
        self.my_booking_button = self.driver.find_element_by_xpath('//*[@id="header"]/div/div[1]/ul/li[2]/a')
        self.site_sign_in_button = self.driver.find_element_by_xpath('//*[@id="header"]/div/div[1]/ul/li[3]/a')
        self.currency_picker = self.driver.find_element_by_id('current-currency-icon')

    def present(self) -> bool:
        for element in (
                self.logo, self.wish_list_button, self.my_booking_button, self.site_sign_in_button,
                self.currency_picker):
            if not element.is_displayed():
                return False

        return True


class Footer:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.our_promise = self.driver.find_element_by_xpath('/html/body/main/div[12]/div/div[1]/div[1]')
        self.drop_us_a_line = self.driver.find_element_by_xpath(
            '/html/body/main/div[12]/div/div[1]/div[2]/div[2]/div[1]')
        self.give_ua_a_call = self.driver.find_element_by_xpath(
            '/html/body/main/div[12]/div/div[1]/div[2]/div[2]/div[2]')
        self.contact_links_row = self.driver.find_element_by_xpath('/html/body/main/div[12]/div/div[2]/div/div/div')
        self.about_us_link = self.driver.find_element_by_xpath('/html/body/main/div[12]/div/div[4]/div/ul/li[1]/a')
        self.blog_link = self.driver.find_element_by_xpath('/html/body/main/div[12]/div/div[4]/div/ul/li[2]/a')
        self.privacy_policy_link = self.driver.find_element_by_xpath(
            '/html/body/main/div[12]/div/div[4]/div/ul/li[3]/a')
        self.customer_terms_link = self.driver.find_element_by_xpath(
            '/html/body/main/div[12]/div/div[4]/div/ul/li[4]/a')
        self.park_terms_link = self.driver.find_element_by_xpath('/html/body/main/div[12]/div/div[4]/div/ul/li[5]/a')
        self.cookie_policy = self.driver.find_element_by_xpath('/html/body/main/div[12]/div/div[4]/div/ul/li[6]/a')

    def present(self) -> bool:
        for element in (
                self.give_ua_a_call, self.drop_us_a_line, self.our_promise, self.give_ua_a_call, self.contact_links_row,
                self.about_us_link, self.blog_link, self.privacy_policy_link,
                self.customer_terms_link, self.park_terms_link, self.cookie_policy):
            if not element.is_displayed():
                return False

        return True


class Search:
    pass


class Newsletter:
    pass
