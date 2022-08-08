import pytest

@pytest.fixture(scope='session', autouse=True)
def setup(browser):
    if browser=='chrome':
        print('Launch chrome')
    elif browser=='ff':
        print("Launch Firefox")
    print("launch")
    print("login")
    print("Browser Product")
    yield
    print("log off")
    print("close browser")
def pytest_addoption(parser):
    parser.addoption("--browser")
@pytest.fixture(scope='session', autouse=True)
def browser(request):
    return request.config.getoption("--browser")