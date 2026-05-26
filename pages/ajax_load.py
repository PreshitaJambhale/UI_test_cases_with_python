from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utilities.utilities import Utils


class AjaxLoad():

    button_path = (By.XPATH, "//button[@id='ajaxButton']")
    ajax_loaded_path = (By.XPATH, "(//p[@class='bg-success'][normalize-space()='Data loaded with AJAX get request.'])[1]")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 30)
        self.uc = Utils(self.driver)

    def wait_and_click(self):
        self.wait.until(EC.element_to_be_clickable(self.button_path)).click()
        self.uc.check_visibility_func(self.ajax_loaded_path)


