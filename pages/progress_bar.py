import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from utilities.utilities import Utils

class ProgressBar():

    start_button = (By.XPATH, "(//button[normalize-space()='Start'])[1]")
    stop_button = (By.XPATH, "//button[@id='stopButton']")
    progress_bar_path = (By.XPATH, f"//div[@role='progressbar' and @aria-valuenow='{range}']")


    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.uc = Utils(self.driver)

    def handle_progress_bar(self, range = 77):
        self.uc.is_element_clickable(self.start_button)
        while True:
            value = int(
                self.driver.find_element(By.XPATH, f"//div[@role='progressbar' and @aria-valuenow='{range}']" )
                .get_attribute("aria-valuenow")
            )
            time.sleep(20)
            if value >= range:
                self.uc.is_element_clickable(self.stop_button).click()
                break

        final_value = 75
        assert abs(final_value - 75) >= 3





