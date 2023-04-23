from common.poco_api import poco_api
import time

class Main_Pages(poco_api):
    searchBar = "com.netease.cloudmusic:id/searchBar"
    search_src_text = "com.netease.cloudmusic:id/search_src_text"
    actionView = "com.netease.cloudmusic:id/actionView"
    recognizeBtn = 'text=搜索'

    def search_test(self, args):
        self.wait_ele(self.searchBar)
        self.click_ele(self.searchBar)

        self.wait_ele(self.search_src_text)
        self.input_ele(self.search_src_text, args)

        # self.wait_ele(self.recognizeBtn)
        self.click_ele(self.recognizeBtn)

        self.wait_ele(self.actionView)
        self.click_ele(self.actionView)
