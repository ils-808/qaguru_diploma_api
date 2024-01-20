import requests
from allure_commons._allure import step


def authorize_user(url, customer):
    with step('Authorize user'):
        return requests.post(url, json=customer)
