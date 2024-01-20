import requests
from allure_commons._allure import step


def booking_list(url):
    with step('Get list of bookings'):
        return requests.get(url)


def delete_booking(url, cookie):
    with step(f'Delete booking {url}'):
        return requests.delete(url, cookies=cookie)


def create_booking(url, booking):
    with step('Create new booking'):
        return requests.post(url, json=booking)


def get_booking_details(url):
    with step('Get booking details'):
        return requests.get(url)


def update_booking_details(url, booking, cookie):
    with step('Update booking details'):
        return requests.put(url, json=booking, cookies=cookie, headers={"Accept": "application/json"})
