from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utilities.utilities import Utils



class DynamicTable():

    columnheader_path = (By.XPATH, "/html/body/section/div/div/div[2]")
    rows_path = (By.XPATH, "/html/body/section/div/div/div[3]/div")
    cells_path = (By.XPATH, "/html/body/section/div/div/div[3]/div/span")
    warning_path = (By.XPATH, "//p[@class='bg-warning']")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.uc = Utils(self.driver)

    def compare_values(self):
        self.uc.read_table(self.columnheader_path, self.rows_path, self.cells_path)
        new_list, columns = self.uc.read_table(self.columnheader_path, self.rows_path, self.cells_path)
        print(new_list, columns)
        self.uc.compare_data_using_pandas(self.warning_path,new_list, columns)



