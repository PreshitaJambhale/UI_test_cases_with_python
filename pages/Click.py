from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utilities.utilities import Utils


class Click():

    bad_button_path = (By.XPATH, "//button[@id='badButton']")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.uc = Utils(self.driver)

    def click(self):
        self.wait.until(EC.element_to_be_clickable(self.bad_button_path)).click()
        self.uc.is_element_clickable(self.bad_button_path)
