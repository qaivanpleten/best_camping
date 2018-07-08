import time

from camp_at.pages.common_elements import Navbar, Footer
from camp_at.pages.home_page import HomePage, WhereDoYouWantToGo, DatePicker, Children
# @pytest.allure.severity(pytest.allure.severity_level.NORMAL)
# @allure.feature('Search campsites by country')
# @allure.stiry('Search')
from camp_at.pages.search_result_page import SearchResultPage


def test_search_camp_by_country(fixture_webdriver):
    HomePage(fixture_webdriver).open()
    assert Navbar(fixture_webdriver).present(), "One or several elements in the Navbar aren't presented"
    assert Footer(fixture_webdriver).present(), "One or several elements in the Footer aren't presented"
    assert HomePage(fixture_webdriver).check_url(), "The URL isn't correct"

    WhereDoYouWantToGo(fixture_webdriver).select_country_autocomplete()
    assert WhereDoYouWantToGo(
        fixture_webdriver).location_is_set(), "Chosen location isn't presented in the Location field"

    DatePicker(fixture_webdriver).set_the_date()
    # assert DatePicker(fixture_webdriver).check_in_is_set(), "The wrong date is set or the date isn't displayed"

    Children(fixture_webdriver).set_number()
    assert Children(fixture_webdriver).number_of_children_is_set(), "Number of children is wrong or isn't set"

    HomePage(fixture_webdriver).perform_search()
    time.sleep(10)
    assert SearchResultPage(fixture_webdriver).check_page_title('Belgium'), "There is the wrong country in result"
