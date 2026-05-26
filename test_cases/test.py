import time
from symtable import Class

import allure
import pytest
from selenium.webdriver.common.by import By

from pages.Click import Click
from pages.ajax_load import AjaxLoad
from pages.alerts import Alerts
from pages.animated_button import AnimatedButton
from pages.classic_attribute_page import ClassicAttribute
from pages.dynamic_table import DynamicTable
from pages.file_upload import FileUpload
from pages.hidden_layers import HiddenLayers
from pages.load_delay import LoadDelay
from pages.mouse_action import MouseAction
from pages.progress_bar import ProgressBar
from pages.sample_file import SampleFile
from pages.scrollbars import ScrollBars
from pages.shadowdom import ShadowDom
from pages.test_input import TextInput
from pages.view_page import ViewPage
from pages.dynamic_ID_page import DynamicID
from pages.visibility import Visibility
from utilities.utilities import Utils


@pytest.mark.usefixtures("setup")
class TestViewPage():

    @pytest.fixture(autouse=True)
    def init_utils(self, setup):
        self.ut = Utils(self.driver)


    def test_elements_presence(self):
        vp = ViewPage(self.driver)

        self.ut.enter_page( "http://www.uitestingplayground.com/")
        vp.check_visibility_of_elements()

    def test_button_is_clickable(self):
        dy = DynamicID(self.driver)
        
        self.ut.enter_page( "http://www.uitestingplayground.com/dynamicid")
        dy.click_elements()
    
    def test_alert_buttons(self):
        ca = ClassicAttribute(self.driver)
        hl = HiddenLayers(self.driver)
        ld = LoadDelay(self.driver)
        al = AjaxLoad(self.driver)
        cl = Click(self.driver)
        ti = TextInput(self.driver)
        sc = ScrollBars(self.driver)

        self.ut.enter_page("http://www.uitestingplayground.com/classattr")
        ca.classic_attribute_addition()
        self.ut.enter_page("http://www.uitestingplayground.com/hiddenlayers")
        hl.hidden_button()
        self.ut.enter_page("http://www.uitestingplayground.com/loaddelay")
        ld.wait_for_button()
        self.ut.enter_page("http://www.uitestingplayground.com/ajax")
        al.wait_and_click()
        self.ut.enter_page("http://www.uitestingplayground.com/click")
        cl.click()
        self.ut.enter_page("http://www.uitestingplayground.com/textinput")
        ti.add_text("test")
        self.ut.enter_page("http://www.uitestingplayground.com/scrollbars")
        sc.scroll_bar()
        
    def test_dynamic_table(self):
        dt = DynamicTable(self.driver)

        self.ut.enter_page("http://www.uitestingplayground.com/dynamictable")
        dt.compare_values()
 
    def test_progress_bar(self):
        pb = ProgressBar(self.driver)
        self.ut.enter_page("http://www.uitestingplayground.com/progressbar")
        pb.handle_progress_bar(range = 75)
       
    def test_visibilty(self):
        vs = Visibility(self.driver)
        self.ut.enter_page("http://www.uitestingplayground.com/visibility")
        vs.check_visibility()



