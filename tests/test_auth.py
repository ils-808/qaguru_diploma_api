import json

import allure
import pytest

from api_handler.authorize import authorize_user
from model.auth import UserAuthReq, UserAuthRes
from model.error import ErrorRes


@allure.story('Authorization')
@allure.title('Success authorization')
@allure.label('layer', 'api')
@allure.tag('smoke')
@pytest.mark.parametrize('login, pwd', [('admin', 'password123')])
def test_login_success(set_url, login, pwd):
    user_creds = UserAuthReq(username=login, password=pwd)
    token = authorize_user(set_url + 'auth', user_creds.model_dump())
    assert token.status_code == 200
    assert UserAuthRes.model_validate_json(json.dumps(token.json()))


@allure.story('Authorization')
@allure.title('Failed authorization')
@allure.label('layer', 'api')
@allure.tag('smoke')
@pytest.mark.parametrize('login, pwd', [('admin', '123password123')])
def test_login_failure(set_url, login, pwd):
    user_creds = UserAuthReq(username=login, password=pwd)
    token = authorize_user(set_url + 'auth', user_creds.model_dump())
    error = ErrorRes.model_validate(token.json())

    assert token.status_code == 200
    assert error.reason == 'Bad credentials'
