from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait




from utilities.utilities import Utils

class Visibility():
    hide_path = (By.XPATH, "//button[@id='hideButton']")
    removed_path = (By.XPATH, "//button[@id='removedButton']")
    zero_width_path = (By.XPATH, "//button[@id='zeroWidthButton']")
    overlapped_path = (By.XPATH, "//button[@id='overlappedButton']")
    opacity0_path = (By.XPATH, "//button[@id='transparentButton']")
    visibility_hidden_path = (By.XPATH, "//button[@id='invisibleButton']")
    display_none_path = (By.XPATH, "//button[@id='notdisplayedButton']")
    offscreen_path = (By.XPATH, "//button[@id='offscreenButton']")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.uc = Utils(self.driver)

    """
    def check_visibility(self):

        self.driver.find_element(*self.hide_path).click()
        removed_element = self.driver.find_element(*self.removed_path)
        zero_width_element = self.driver.find_element(*self.zero_width_path)
        overlapped_element = self.driver.find_element(*self.overlapped_path)
        opacity0_element = self.driver.find_element(*self.opacity0_path)
        visibility_hidden_element = self.driver.find_element(*self.visibility_hidden_path)
        display_none_element = self.driver.find_element(*self.display_none_path)
        offscreen_element = self.driver.find_element(*self.offscreen_path)
        with verify():  # All 'check' failures within this block are collected
            check( removed_element.is_displayed(), "removed element is not visible")
            check( zero_width_element.is_displayed(), "zero width element is not visible")
            check( overlapped_element.is_displayed(), "overlapped element is not visible")
            check( opacity0_element.is_displayed(), "Opacity 0 element is not visible")
            check( visibility_hidden_element.is_displayed(), "visibility element is not visible")
            check( display_none_element.is_displayed(), "display none element is not visible")
            check( offscreen_element.is_displayed(), "offscreen element is not visible")
        
        """
    def check_visibility(self):
        self.driver.find_element(*self.hide_path).click()

        with verify():
            self.uc.soft_check_visibility(self.removed_path, "removed element")
            self.uc.soft_check_visibility(self.zero_width_path, "zero width element")
            self.uc.soft_check_visibility(self.overlapped_path, "overlapped element")
            self.uc.soft_check_visibility(self.opacity0_path, "opacity 0 element")
            self.uc.soft_check_visibility(self.visibility_hidden_path, "visibility hidden element")
            self.uc.soft_check_visibility(self.display_none_path, "display none element")
            self.uc.soft_check_visibility(self.offscreen_path, "offscreen element")

