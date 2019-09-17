import os, sys
import time

import allure
import pytest

sys.path.append(os.getcwd())

from base.base_yml import yml_data_with_filename_and_key

from base.base_driver import init_driver

from page.page_login import Page_login

def data_with_key(key):
    return yml_data_with_filename_and_key("login_data", key)

class Test_login:
    def setup(self):
        self.driver = init_driver()
        self.page = Page_login(self.driver)
    def teardown(self):
        self.driver.quit()
    allure.step(title="测试登录模块")
    @pytest.mark.parametrize("args",data_with_key("test_login"))
    def test_login(self, args):
        allure.attach("用户名", args["username"])
        self.page.input_login_name(args["username"])
        allure.attach("密码", args["password"])
        self.page.input_login_pwd(args["password"])
        self.page.click_login_button()
        allure.attach("断言", "")
        assert self.page.is_toast_exist(args["toast"])