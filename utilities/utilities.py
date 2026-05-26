import os

from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import pandas as pd
from soft_assert import check, verify
from selenium.webdriver.common.action_chains import ActionChains
import pyperclip

class Utils():

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

        ''' add url to enter a page'''
    def enter_page(self, url):
        self.driver.get(url)

        """check whether element is visible"""
    def check_visibility_func(self, path):
        element = self.wait.until(EC.visibility_of_element_located(path))
        print("done")
        assert element.is_displayed()

        """check whether element is clickable"""

    def is_element_clickable(self, path):
        element =self.wait.until(EC.visibility_of_element_located(path))
        element.click()
        assert element.is_displayed(), "element is not clickable"
        assert element.is_enabled()
        print("element is clickable")

        """check whether button is primary"""
    def check_primary(self,path):
        element = self.wait.until(EC.element_to_be_clickable(path))
        element.click()
        if "btn-primary" in path[1]:
            alert = self.wait.until(EC.alert_is_present())
            assert alert.text == "Primary button pressed", "Alert text mismatch"
            alert.accept()
        else:
            print("not a primary button")

        """read the data in the table and return a list of all data along with columns present"""
    def read_table(self,column_path, row_path, cell_path):
        wait = WebDriverWait(self.driver, 10)
        headers = self.wait.until(EC.presence_of_all_elements_located(column_path))
        column_names = [h.text for h in headers]
        columns = column_names[0].split()

        rows = self.wait.until(EC.presence_of_all_elements_located(row_path))

        table_data = []
        for row in rows:
            cells = row.find_elements(*cell_path)
            row_data = [cell.text for cell in cells]
            table_data.append(row_data)

        num_cols = 5
        new_list = [
            table_data[0][i:i + num_cols]
        for i in range(0, len(table_data[0]), num_cols)
        ]
        return new_list, columns

        """Compare data using pandas"""
    def compare_data_using_pandas(self,path, new_list,columns ):
        df = pd.DataFrame(new_list, columns=columns)
        chrome_cpu = df.loc[df["Name"] == "Chrome", "CPU"].values[0]
        label = self.wait.until(EC.element_to_be_clickable(path)).text
        print(label)

        assert chrome_cpu in label

    """soft check for visibilty"""
    def soft_check_visibility(self, locator, name):
        elements = self.driver.find_elements(*locator)

        if not elements:
            check(False, f"{name} not found in DOM")
        else:
            check(
                elements[0].is_displayed(),
                f"{name} is not visible"
            )

    """login function"""
    def check_login_func(self, locator):

        text = self.driver.find_element(*locator).text
        print(text)
        assert text == "Welcome, test!", "user logged in successfully"

    """Click using mouse multiple times"""
    def mouse_click(self, locator1, locator2,number_of_clicks):
        actions = ActionChains(self.driver)
        i = 0
        while i <= number_of_clicks:
            element1 = self.driver.find_element(*locator1)
            actions.move_to_element(element1).click().perform()
            element2 = self.driver.find_element(*locator2)
            actions.move_to_element(element2).click().perform()
            i +=1

    """copy values from clipboard"""
    def copy_from_clipboard(self):
        clipboard_value = pyperclip.paste()
        return clipboard_value

    """click using action chains"""
    def action_chain_click(self, locator):
        actions = ActionChains(self.driver)
        element = self.driver.find_element(*locator)
        actions.move_to_element(element).click().perform()

    """send keys using action chains"""
    def action_chain_send_keys(self, locator, value):
        actions = ActionChains(self.driver)
        element = self.driver.find_element(*locator)
        actions.send_keys_to_element(element, value).perform()

    """interact using JS"""
    def execute_js(self, locator):
        element = self.driver.execute_script(locator)
        element.click()
        return element

    """accept an alert"""
    def alert_accept(self, timeout = 5):
        element = WebDriverWait(self.driver, timeout).until(EC.alert_is_present())
        element.accept()

    """dismiss an alert"""
    def alert_dismiss(self, timeout = 5):
        element = WebDriverWait(self.driver, timeout).until(EC.alert_is_present())
        element.dismiss()

    """send keys an alert"""
    def alert_send_keys(self, value, timeout = 5 ):
        element = WebDriverWait(self.driver, timeout).until(EC.alert_is_present())
        element.send_keys(value)

    """get text from an alert"""
    def alert_get_text(self):
        alert = self.driver.switch_to.alert
        alert_text = alert.text
        print(alert_text)

    def upload_files(self, locator):
        document = "/Users/harshalijambhale/Documents/Book1.xlsx"
        self.driver.find_element(*locator).send_keys(document)















