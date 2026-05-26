"""all the links on the view page are available here"""

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utilities.utilities import Utils


class ViewPage():

    url = "http://www.uitestingplayground.com/"
    dynamicID_path = (By.XPATH, "//a[normalize-space()='Dynamic ID']")
    class_attribute_path = (By.XPATH, "//a[normalize-space()='Class Attribute']")
    hidden_layers_path = (By.XPATH, "//a[normalize-space()='Hidden Layers']")
    load_delay_path = (By.XPATH, "//a[normalize-space()='Load Delay']")
    Ajax_data_path = (By.XPATH, "//a[normalize-space()='AJAX Data']")
    client_side_delay_path = (By.XPATH, "//a[normalize-space()='Client Side Delay']")
    click_path = (By.XPATH, "//a[normalize-space()='Click']")
    text_input = (By.XPATH, "//a[normalize-space()='Text Input']")
    scrollbars_path = (By.XPATH, "//a[normalize-space()='Scrollbars']")
    dynamic_table_path = (By.XPATH, "//a[normalize-space()='Dynamic Table']")
    verify_path = (By.XPATH, "//a[normalize-space()='Verify Text']")
    progress_path = (By.XPATH, "//a[normalize-space()='Verify Text']")
    visibility_path = (By.XPATH, "//a[normalize-space()='Visibility']")
    sample_app_path = (By.XPATH, "//a[normalize-space()='Sample App']")
    mouse_path = (By.XPATH, "//a[normalize-space()='Mouse Over']")
    nonBreaking_space_path = (By.XPATH, "//a[normalize-space()='Non-Breaking Space']")
    overlapped_ele_path = (By.XPATH, "//a[normalize-space()='Overlapped Element']")
    shadow_dom_path = (By.XPATH, "//a[normalize-space()='Shadow DOM']")
    alerts_path = (By.XPATH, "//a[normalize-space()='Alerts']")
    filepath_path = (By.XPATH, "//a[normalize-space()='File Upload']")
    animated_path = (By.XPATH, "//a[normalize-space()='Animated Button']")
    disabled_path = (By.XPATH, "//a[normalize-space()='Disabled Input']")
    auto_wait_path = (By.XPATH, "//a[normalize-space()='Auto Wait']")



    def __init__(self, driver):

        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.uc = Utils(self.driver)

    def enter_page(self):
        self.driver.get(self.url)



    def check_visibility_of_elements(self):
        self.uc.check_visibility_func(self.dynamicID_path)
        self.uc.check_visibility_func(self.class_attribute_path)
        self.uc.check_visibility_func(self.hidden_layers_path)
        self.uc.check_visibility_func(self.load_delay_path)
        self.uc.check_visibility_func(self.Ajax_data_path)
        self.uc.check_visibility_func(self.client_side_delay_path)
        self.uc.check_visibility_func(self.click_path)
        self.uc.check_visibility_func(self.text_input)
        self.uc.check_visibility_func(self.scrollbars_path)
        self.uc.check_visibility_func(self.dynamic_table_path)
        self.uc.check_visibility_func(self.verify_path)
        self.uc.check_visibility_func(self.progress_path)
        self.uc.check_visibility_func(self.visibility_path)
        self.uc.check_visibility_func(self.sample_app_path)
        self.uc.check_visibility_func(self.mouse_path)
        self.uc.check_visibility_func(self.nonBreaking_space_path)
        self.uc.check_visibility_func(self.overlapped_ele_path)
        self.uc.check_visibility_func(self.shadow_dom_path)
        self.uc.check_visibility_func(self.alerts_path)
        self.uc.check_visibility_func(self.filepath_path)
        self.uc.check_visibility_func(self.animated_path)
        self.uc.check_visibility_func(self.auto_wait_path)



