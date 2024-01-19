import json

import allure
import pytest
from allure_commons._allure import step

from api_handler.authorize import authorize_user
from model.auth import UserAuthReq, UserAuthRes
from model.error import ErrorRes


@allure.story('Authorization')
@allure.title('Success authorization')
@allure.label('layer', 'api')
@allure.tag('smoke')
@pytest.mark.api
@pytest.mark.parametrize('login, pwd', [('admin', 'password123')])
def test_login_success(set_url, login, pwd):
    user_creds = UserAuthReq(username=login, password=pwd)
    with step('Attempt to authorize user successfully'):
        token = authorize_user(set_url + 'auth', user_creds.model_dump())

    with step('Validate response code 200'):
        assert token.status_code == 200
    with step('Validate response schema'):
        assert UserAuthRes.model_validate(token.json())
    with step('Validate value of response'):
        assert str(token.text).startswith('{"token":', 0)


@allure.story('Authorization')
@allure.title('Failed authorization')
@allure.label('layer', 'api')
@allure.tag('smoke')
@pytest.mark.api
@pytest.mark.parametrize('login, pwd', [('admin', '123password123')])
def test_login_failure(set_url, login, pwd):
    user_creds = UserAuthReq(username=login, password=pwd)
    with step('Attempt to authorize user unsuccessfully'):
        token = authorize_user(set_url + 'auth', user_creds.model_dump())

    with step('Validate response schema'):
        error = ErrorRes.model_validate(token.json())
    with step('Validate response code 200'):
        assert token.status_code == 200
    with step('Validate value of response'):
        assert error.reason == 'Bad credentials'
