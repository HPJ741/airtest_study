import logging

import pytest


@pytest.fixture(scope="session",autouse=True)
def session_module():
    logger = logging.getLogger("airtest")
    logger.setLevel(logging.INFO)
    logging.info("**************开始测试**************")
    yield
    logging.info("**************测试结束**************")

