import time

from camp_at.pages.common_elements import Navbar, Footer
from camp_at.pages.home_page import HomePage, WhereDoYouWantToGo, DatePicker


# @pytest.allure.severity(pytest.allure.severity_level.NORMAL)
# @allure.feature('Search campsites by country')
# @allure.stiry('Search')
def test_search_camp_by_country(fixture_webdriver):
    HomePage(fixture_webdriver).open()
    assert Navbar(fixture_webdriver).present(), "One or several elements in the Navbar aren't presented"
    assert Footer(fixture_webdriver).present(), "One or several elements in the Footer aren't presented"
    assert HomePage(fixture_webdriver).check_url(), "The URL isn't correct"

    time.sleep(3)

    WhereDoYouWantToGo(fixture_webdriver).select_country_autocomplete()
    assert WhereDoYouWantToGo(
        fixture_webdriver).location_is_set(), "Chosen location isn't prsented in the Location field"

    time.sleep(3)

    DatePicker(fixture_webdriver).set_the_date()

    time.sleep(3)