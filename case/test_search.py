import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

import logging
import threading

from airtest.core.api import *
from poco.drivers.android.uiautomation import AndroidUiautomationPoco

from pages.Main_Pages import Main_Pages
from pages.login_api import Login


def find_ANR(poco):
    while True:
        logging.info("异常处理线程正常运行中-------")
        if poco("android:id/aerr_wait").exists():
            poco("android:id/aerr_wait").click()

        if poco("com.android.packageinstaller:id/permission_allow_button").exists():
            poco("com.android.packageinstaller:id/permission_allow_button").click()

        if poco(text="仅在使用中允许").exists():
            poco(text="仅在使用中允许").click()

        time.sleep(5)


class Test_wangyiyun:
    poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)

    def setup_class(self):
        auto_setup(__file__, devices=[
            "android://127.0.0.1:5037/1268b147?cap_method=MINICAP&ori_method=ADBORI&touch_method=MAXTOUCH&"])
        self.l = Login(self.poco)
        self.m = Main_Pages(self.poco)

        thread = threading.Thread(target=find_ANR, args=(self.poco,))
        thread.daemon = True
        thread.start()

        clear_app("com.netease.cloudmusic")
        start_app("com.netease.cloudmusic")

    def teardown_class(self):
        pass

    def test_login(self):
        self.l.login_test()
        self.l.save_screen(filename="test_login.png")

    def test_search(self):
        self.m.search_test("有何不可")
        self.m.save_screen(filename="test_search.png")
