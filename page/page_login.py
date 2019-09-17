import os, sys
import time

import pytest
from selenium.webdriver.common.by import By

sys.path.append(os.getcwd())

from base.base_action import BaseAction

class Page_login(BaseAction):
    my_button = By.XPATH, "text,我的"
    login_input_button = By.ID, "com.tpshop.malls:id/head_img"
    login_name = By.ID, "com.tpshop.malls:id/mobile_et"
    login_pwd = By.ID, "com.tpshop.malls:id/pwd_et"
    login_button = By.ID, "com.tpshop.malls:id/login_tv"

    def __init__(self, driver):
        BaseAction.__init__(self, driver)
        self.jump_2_page_login()
    def jump_2_page_login(self):
        self.click(self.my_button)
        self.click(self.login_input_button)
    def input_login_name(self, text):
        self.input_text(self.login_name, text)
    def input_login_pwd(self, text):
        self.input_text(self.login_pwd, text)
    def click_login_button(self):
        self.click(self.login_button)
