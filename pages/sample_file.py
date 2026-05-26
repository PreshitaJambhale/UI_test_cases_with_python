
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from utilities.utilities import Utils


class SampleFile():

    text_path = (By.XPATH, "//label[@id='loginstatus']")
    username_path = (By.XPATH, "//input[@placeholder='User Name']")
    password_path = (By.XPATH, "//input[@type='password']")
    login_button_path = (By.XPATH, "//button[@id='login']")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.uc = Utils(self.driver)

    def check_login(self, username, password):
        self.wait.until(EC.element_to_be_clickable(self.username_path)).send_keys(username)
        self.wait.until(EC.element_to_be_clickable(self.password_path)).send_keys(password)
        self.wait.until(EC.element_to_be_clickable(self.login_button_path)).click()
        self.uc.check_login_func(self.text_path)





