from common.poco_api import poco_api

class Login(poco_api):
    agree_ele = "com.netease.cloudmusic:id/agree"
    trialT_ele = "com.netease.cloudmusic:id/trialT"
    positveBtn_ele = "com.netease.cloudmusic:id/positiveBtn"

    def login_test(self):
        self.wait_ele(self.agree_ele)
        if self.exit_ele(self.agree_ele):
            self.click_ele(self.agree_ele)

        self.wait_ele(self.trialT_ele)
        self.click_ele(self.trialT_ele)

        self.wait_ele(self.positveBtn_ele)
        self.click_ele(self.positveBtn_ele)


