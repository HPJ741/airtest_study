from poco.drivers.android.uiautomation import AndroidUiautomationPoco
import os
import allure
from airtest.core.api import *

class poco_api:

    def __init__(self,poco):
        self.poco = poco

    def locate_ele(self, args):
        if "=" in args:
            args = args.split("=")
            if args[0] == "text":
                return self.poco(text=args[1])
        else:
            return self.poco(args)

    def wait_ele(self, args):
        self.locate_ele(args).wait_for_appearance()

    def exit_ele(self, args):
        return self.locate_ele(args).exists()

    def input_ele(self, args, text=None):
        self.locate_ele(args).set_text(text)

    def click_ele(self, args):
        self.locate_ele(args).click([0.5, 0.5])

    def drag_to_ele(self, from_args, to_args):
        self.locate_ele(from_args).drag_to(to_args)

    def swipe_up_ele(self, args):
        self.locate_ele(args).swipe([0, -0.5])

    def swipe_down_ele(self, args):
        self.locate_ele(args).swipe([0, 0.5])

    def swipe_right_ele(self, args):
        self.locate_ele(args).swipe([-0.4, 0])

    def swipe_left_ele(self, args):
        self.locate_ele(args).swipe([0.4, 0])

    def save_screen(self, filename):
        root_path = "img"
        filepath = os.path.join(root_path, filename)
        snapshot(filename=filepath)
        with open(filepath, 'rb') as f:
            allure.attach(f.read(), filename, allure.attachment_type.PNG)
