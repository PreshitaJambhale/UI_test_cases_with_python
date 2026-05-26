
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from utilities.utilities import Utils


class MouseAction():

    link_path = (By.XPATH, "//a[normalize-space()='Click me']")
    button_path = (By.XPATH, "//a[normalize-space()='Link Button']")
    link_number_path = (By.XPATH, "//span[@id='clickCount']")
    button_number_path = (By.XPATH, "//span[@id='clickButtonCount']")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.uc = Utils(self.driver)

    def check_mouse_click(self):
        self.uc.mouse_click(self.link_path, self.button_path, 1)
        click_link_rate = int(self.driver.find_element(*self.link_number_path).text)
        button_click_rate = int(self.driver.find_element(*self.button_number_path).text)
        print(click_link_rate, button_click_rate)
        assert click_link_rate == 2, "incorrect number of clicks"
        assert button_click_rate == 2, "incorrect number of clicks"