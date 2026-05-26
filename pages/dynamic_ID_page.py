

"""handling dynamic ID"""
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utilities.utilities import Utils


class DynamicID():

    index_based_path = (By.XPATH, "(//button[normalize-space()='Button with Dynamic ID'])[1]")
    abs_based_path = (By.XPATH, "/html[1]/body[1]/section[1]/div[1]/button[1]")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.uc =  Utils(self.driver)



    def click_elements(self):
        #self.uc.is_element_clickable(self.text_based_path)
        self.uc.is_element_clickable(self.index_based_path)
        self.uc.is_element_clickable(self.abs_based_path)

