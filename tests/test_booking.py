import json

import allure
import pytest

from api_handler.authorize import authorize_user
from api_handler.booking import booking_list, delete_booking, create_booking
from model.auth import UserAuthReq, UserAuthRes
from model.booking import BookingListRes, BookingCreateReq, BookingDates, BookingCreateRes


@allure.story('Booking')
@allure.title('List all booking')
@allure.label('layer', 'api')
@allure.tag('smoke')
@pytest.mark.api
def test_booking_list(set_url):
    res = booking_list(set_url + 'booking')

    assert res.status_code == 200
    assert BookingListRes.model_validate_json(json.dumps(res.json()))


@allure.story('Booking')
@allure.title('Delete booking')
@allure.label('layer', 'api')
@allure.tag('smoke')
@pytest.mark.api
@pytest.mark.parametrize('login, pwd',
                         [('admin', 'password123')])
def test_booking_deletion(set_url, login, pwd):
    user_creds = UserAuthReq(username=login, password=pwd)
    token = authorize_user(set_url + 'auth', user_creds.model_dump())

    bookings = BookingListRes(booking_list(set_url + 'booking').json())

    id_to_delete = bookings.root[0].bookingid
    res = delete_booking(set_url + f'booking/{id_to_delete}', token.json())

    assert res.status_code == 201
    assert res.text == 'Created'


@allure.story('Booking')
@allure.title('Create booking')
@allure.label('layer', 'api')
@allure.tag('smoke')
@pytest.mark.api
@pytest.mark.parametrize('firstname, lastname, totalprice, depositpaid, checkin, checkout, additionalneeds',
                         [('jim', 'brown', 111, True, '2018-01-01', '2019-01-01', 'Breakfast')])
def test_booking_creation(set_url, firstname, lastname, totalprice, depositpaid, checkin,
                          checkout,
                          additionalneeds):
    dates = BookingDates(checkin=checkin,
                         checkout=checkout)

    reserve = BookingCreateReq(firstname=firstname,
                            lastname=lastname,
                            totalprice=totalprice,
                            depositpaid=depositpaid,
                            bookingdates=dates,
                            additionalneeds=additionalneeds
                            )
    bookings_res = create_booking(set_url + 'booking', reserve.model_dump())
    booking_model = BookingCreateRes.model_validate(bookings_res.json())

    assert bookings_res.status_code == 200
    assert booking_model.bookingid != 0
