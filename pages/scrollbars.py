from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utilities.utilities import Utils

class ScrollBars():

    hidden_button_path = (By.XPATH, "//button[@id='hidingButton']")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.uc = Utils(self.driver)

    def scroll_bar(self):
        element = self.wait.until(EC.element_to_be_clickable(self.hidden_button_path))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        self.wait.until(EC.element_to_be_clickable(self.hidden_button_path)).click()
        self.uc.is_element_clickable(self.hidden_button_path)