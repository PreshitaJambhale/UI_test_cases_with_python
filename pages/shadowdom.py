import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from utilities.utilities import Utils


class ShadowDom():

    generate_path = (''' return document.querySelector('guid-generator').
    shadowRoot.querySelector('#buttonGenerate')''')
    copy_path = (''' return document.querySelector('guid-generator').
    shadowRoot.querySelector('#buttonCopy')''')
    input_path = (''' return document.querySelector('guid-generator').
    shadowRoot.querySelector("#editField")''')


    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.uc = Utils(self.driver)

    def compare_with_shadowdom(self):
        self.uc.execute_js(self.generate_path)
        self.uc.execute_js(self.copy_path)
        input_field = self.uc.execute_js(self.input_path)
        text = input_field.get_property("value")
        print(text)
        copied_value= self.uc.copy_from_clipboard()
        print(self.uc.copy_from_clipboard())
        print(copied_value)
        assert copied_value == text, "copied value and generated value do not match"