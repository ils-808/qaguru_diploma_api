import allure
import pytest
from allure_commons._allure import step

from restful_booker_project_tests.api_handler.authorize import authorize_user
from restful_booker_project_tests.api_handler.booking import booking_list, delete_booking, create_booking, \
    get_booking_details, \
    update_booking_details
from restful_booker_project_tests.model.auth import UserAuthReq
from restful_booker_project_tests.model.booking import BookingListRes, BookingCreateReq, BookingDates, BookingCreateRes


@allure.story('Booking')
@allure.title('List all booking')
@allure.label('layer', 'api')
@allure.tag('smoke')
@pytest.mark.api
def test_booking_list(set_url):
    res = booking_list(set_url + 'booking')
    data = BookingListRes(res.json())

    #d = BookingListRes.model_dump(res.json(), by_alias=True)

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
    bookings = BookingListRes(root=booking_list(set_url + 'booking').json())

    user_creds = UserAuthReq(username=login, password=pwd)
    token = authorize_user(set_url + 'auth', user_creds.model_dump())

    id_to_delete = bookings.root[0].booking_id
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
@pytest.mark.parametrize('firstname, lastname, total_price, deposit_paid, checkin, checkout, additional_needs',
                         [('jim', 'brown', 111, True, '2018-01-01', '2019-01-01', 'Breakfast')])
def test_booking_creation(set_url, firstname, lastname, total_price, deposit_paid, checkin,
                          checkout,
                          additional_needs):
    dates = BookingDates(checkin=checkin,
                         checkout=checkout)

    reserve = BookingCreateReq(firstname=firstname,
                               lastname=lastname,
                               total_price=total_price,
                               deposit_paid=deposit_paid,
                               booking_dates=dates,
                               additional_needs=additional_needs
                               )
    bookings_res = create_booking(set_url + 'booking', reserve.model_dump(by_alias=True))
    booking_model = BookingCreateRes.model_validate(bookings_res.json())

    with step('Validate response schema'):
        BookingCreateRes.model_validate(bookings_res.json())
    with step('Validate response code 200'):
        assert bookings_res.status_code == 200
    with step('Validate value of response'):
        assert booking_model.booking_id != 0


@allure.story('Booking')
@allure.title('Update booking')
@allure.label('layer', 'api')
@allure.tag('smoke')
@pytest.mark.api
@pytest.mark.parametrize('login, pwd, firstname, lastname',
                         [('admin', 'password123', 'ilya', 'ilya')])
def test_booking_update(set_url, login, pwd, firstname, lastname):
    user_creds = UserAuthReq(username=login, password=pwd)
    token = authorize_user(set_url + 'auth', user_creds.model_dump())

    bookings = BookingListRes(root=booking_list(set_url + 'booking').json())
    id_to_update = bookings.root[0].booking_id
    details_before_update = get_booking_details(set_url + f'booking/{id_to_update}')
    booking_model_before = BookingCreateReq.model_validate(details_before_update.json())

    booking_model_update = booking_model_before.model_copy()
    booking_model_update.__dict__.update({'firstname': firstname})
    booking_model_update.__dict__.update({'lastname': lastname})

    res = update_booking_details(set_url + f'booking/{id_to_update}', booking_model_update.model_dump(by_alias=True), token.json())

    updated_model = BookingCreateReq.model_validate(res.json())

    with step('Validate response schema'):
        BookingCreateReq.model_validate(res.json())
    with step('Validate response code 200'):
        assert res.status_code == 200
    with step('Validate firstname changed'):
        assert updated_model.firstname != booking_model_before.firstname
    with step('Validate lastname changed'):
        assert updated_model.lastname != booking_model_before.lastname
