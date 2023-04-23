import os

import pytest

if __name__ == "__main__":
    pytest.main(["--alluredir=allure_root/allure_json","--clean-alluredir"])
    os.system("allure generate allure_root/allure_json -o allure_root/allure_reporter --clean")


