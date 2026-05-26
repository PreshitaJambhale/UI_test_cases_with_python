from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from utilities.utilities import Utils


class LoadDelay():

    delayed_button_path = (By.XPATH, "//button[normalize-space()='Button Appearing After Delay']")
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 30)
        self.uc = Utils(self.driver)

    def wait_for_button(self):
        self.wait.until(EC.element_to_be_clickable(self.delayed_button_path))