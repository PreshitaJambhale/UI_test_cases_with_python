import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from utilities.utilities import Utils


class Alerts():

    alert_button_path = (By.XPATH, "//button[@id='alertButton']")
    confirm_path = (By.XPATH, "//button[@id='confirmButton']")
    prompt_path = (By.XPATH, "//button[@id='promptButton']")


    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.uc = Utils(self.driver)

    def interacting_with_alerts(self):
        self.wait.until(EC.element_to_be_clickable(self.alert_button_path)).click()
        self.uc.alert_accept()
        self.driver.find_element(*self.confirm_path).click()
        self.uc.alert_dismiss()
        self.uc.alert_accept()
        self.driver.find_element(*self.prompt_path).click()
        self.uc.alert_send_keys("dogs")
        self.uc.alert_get_text()
        self.uc.alert_accept()
