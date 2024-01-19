import json

import allure
import pytest
from allure_commons._allure import step

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
    data = BookingListRes(res.json())

    with step('Validate response code 200'):
        assert res.status_code == 200
    with step('Validate response schema'):
        assert BookingListRes.model_validate(res.json())
    with step('Validate value of response'):
        assert data.root.pop() is not None


@allure.story('Booking')
@allure.title('Delete booking')
@allure.label('layer', 'api')
@allure.tag('smoke')
@pytest.mark.api
@pytest.mark.parametrize('login, pwd',
                         [('admin', 'password123')])
def test_booking_deletion(set_url, login, pwd):
    bookings = BookingListRes(booking_list(set_url + 'booking').json())

    user_creds = UserAuthReq(username=login, password=pwd)
    token = authorize_user(set_url + 'auth', user_creds.model_dump())

    id_to_delete = bookings.root[0].bookingid
    res = delete_booking(set_url + f'booking/{id_to_delete}', token.json())

    with step('Validate response code 201'):
        assert res.status_code == 201
    with step('Validate value of response'):
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

    with step('Validate response schema'):
        BookingCreateRes.model_validate(bookings_res.json())
    with step('Validate response code 200'):
        assert bookings_res.status_code == 200
    with step('Validate value of response'):
        assert booking_model.bookingid != 0
