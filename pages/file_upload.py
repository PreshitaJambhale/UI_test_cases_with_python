import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from utilities.utilities import Utils


class FileUpload():

    delayed_button_path = (By.XPATH, "//button[normalize-space()='Button Appearing After Delay']")
    frame_path = (By.XPATH, "//iframe[@src='/static/upload.html']")
    add_document_path = (By.XPATH, "//input[@id = 'browse']")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 30)
        self.uc = Utils(self.driver)

    def upload_files(self):
        frame = self.driver.find_element(*self.frame_path)
        self.driver.switch_to.frame(frame)
        #self.driver.find_element(*self.add_document_path)
        self.uc.upload_files(self.add_document_path)
        time.sleep(20)





