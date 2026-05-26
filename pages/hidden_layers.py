
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from utilities.utilities import Utils


class HiddenLayers():

    green_button_path = (By.XPATH, "//button[@id='greenButton']")
    blue_button_path = (By.XPATH, "//button[@id='blueButton']")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.uc = Utils(self.driver)


    def hidden_button(self):
        self.uc.check_visibility_func(self.green_button_path)
        self.driver.find_element(*self.green_button_path).click()
        self.uc.check_visibility_func(self.blue_button_path)
