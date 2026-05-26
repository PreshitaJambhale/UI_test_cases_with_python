from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utilities.utilities import Utils


class TextInput:

    input_path = (By.XPATH, "//input[@id='newButtonName']")
    updating_button_path = (By.XPATH, "//button[@id='updatingButton']")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.uc =  Utils(self.driver)

    def add_text(self, new_button_name):
        self.wait.until(EC.element_to_be_clickable(self.input_path)).send_keys(new_button_name)
        self.wait.until(EC.element_to_be_clickable(self.updating_button_path)).click()
        text1 = self.driver.find_element(*self.updating_button_path).text
        print(text1)
        assert text1 == new_button_name, "name changed"
        print("button name has been changed")



