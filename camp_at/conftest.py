import pytest
from selenium import webdriver


@pytest.fixture
def fixture_webdriver() -> webdriver:
    driver = webdriver.Chrome(
        "C:\\Users\Владелец\PycharmProjects\chromedriver")  # "C:\\Users\Владелец\PycharmProjects\chromedriver" '/home/user/chromedriver'
    driver.maximize_window()
    driver.implicitly_wait(10)

    yield driver
    driver.quit()





