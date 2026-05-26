import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from utilities.utilities import Utils


class AnimatedButton():

    start_delayed_button_path = (By.XPATH, "//button[@id='animationButton']")
    moving_button_path = (By.XPATH, "//button[@class ='btn btn-primary' and  @id='movingTarget']")
    text_path = (By.XPATH, "//div[@id='opstatus']")


    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 30)
        self.uc = Utils(self.driver)

    def animated_button_handle(self):
        self.driver.find_element(*self.start_delayed_button_path).click()
        self.uc.is_element_clickable(self.moving_button_path)
        text = self.driver.find_element(*self.text_path).text
        assert text == "Moving Target clicked. It's class name is 'btn btn-primary'", \
            "button was clicked while in animation"

