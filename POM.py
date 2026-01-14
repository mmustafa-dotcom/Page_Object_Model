import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture
def driver():
    driver=webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

class LoginPage:
    def __init__(self,driver):
        self.driver=driver

    username=(By.ID,"username")
    password=(By.ID,"password")
    login_btn=(By.CSS_SELECTOR, "button[type='submit']")

    def open(self):
        self.driver.get("https://the-internet.herokuapp.com/login")

    def login(self,user,pwd):
        self.driver.find_element(*self.username).send_keys(user)
        self.driver.find_element(*self.password).send_keys(pwd)
        self.driver.find_element(*self.login_btn).click()


def test_login33(driver):
    login=LoginPage(driver)
    login.open()
    login.login("tomsmith","SuperSecretPassword!")

    assert "app" in driver.current_url