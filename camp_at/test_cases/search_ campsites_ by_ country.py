import time
import allure
import pytest

from camp_at.pages.common_elements import Navbar, Footer
from camp_at.pages.home_page import HomePage


# @pytest.allure.severity(pytest.allure.severity_level.NORMAL)
# @allure.feature('Search campsites by country')
# @allure.stiry('Search')
def test_search_camp_by_country(fixture_webdriver):
    HomePage(fixture_webdriver).open()
    assert Navbar(fixture_webdriver).present(), "One or several elements in the Navbar aren't presented"
    assert Footer(fixture_webdriver).present(), "One or several elements in the Footer aren't presented"
    assert HomePage(fixture_webdriver).check_url(), "The URL isn't correct"

    time.sleep(5)


# @pytest.allure.severity(pytest.allure.severity_level.MINOR)
# @allure.feature('Check elements on AboutUs page')
# @allure.story('General elements')
# def test_general_elements(fixture_webdriver):
#     AboutUsPage(fixture_webdriver).open()
#     assert Header(fixture_webdriver).present(), "Header is broken"
#
#
# @pytest.allure.severity(pytest.allure.severity_level.NORMAL)
# @allure.feature('Check elements on AboutUs page')
# @allure.story('AboutUs page elements')
# def test_aboutus_page(fixture_webdriver):
#     AboutUsPage(fixture_webdriver).open()
#     assert Body(fixture_webdriver).present(), "Body is broken, some of the element is missed"
#     assert MeetTheTeamBlock(fixture_webdriver).present(), "Meet hte team block is broken"
#
#
# @pytest.allure.severity(pytest.allure.severity_level.NORMAL)
# @allure.feature('Check elements on AboutUs page')
# @allure.story('AboutUs page buttons')
# def test_buttons(fixture_webdriver):
#     AboutUsPage(fixture_webdriver).open()
#     Button(fixture_webdriver).open_positions().click()
#     time.sleep(1)
#
#     assert not AboutUsPage(fixture_webdriver).check_url(), "The wrong page was opened"
