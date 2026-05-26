
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from utilities.utilities import Utils


class ClassicAttribute():

    green_button_path = (By.XPATH, "//button[   contains(normalize-space(), 'Button')   and contains(@class, 'btn-success') ]")
    yellow_button_path = (By.XPATH, "//button[   contains(normalize-space(), 'Button')   and contains(@class, 'btn-warning') ]")
    blue_button_path = (By.XPATH, "//button[   contains(normalize-space(), 'Button')   and contains(@class, 'btn-primary') ]")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.uc = Utils(self.driver)

    def classic_attribute_addition(self):

        self.uc.check_primary(self.green_button_path)
        self.uc.check_primary(self.yellow_button_path)
        self.uc.check_primary(self.blue_button_path)













#