import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='en',
                     help="Choose language, examples: '--language=en', '--language=ru'")

@pytest.fixture(scope="function")
def browser(request):
    user_language = request.config.getoption("language")

    browser = None
    print("\nstart chrome browser for test..")
    options = ChromeOptions()
    options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
    browser = webdriver.Chrome(options=options)
    yield browser
    print("\nquit browser..")
    browser.quit()

