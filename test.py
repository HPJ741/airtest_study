import allure

def a():
    print("----------------")


with allure.step("测试"):
    print("哈哈哈哈")

with a:
    print("----------------")


