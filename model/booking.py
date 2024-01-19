from typing import List

from pydantic import BaseModel, RootModel


class Booking(BaseModel):
    bookingid: int


class BookingListRes(RootModel):
    root: list[Booking]


class BookingDates(BaseModel):
    checkin: str
    checkout: str


class BookingCreateReq(BaseModel):
    firstname: str
    lastname: str
    totalprice: int
    depositpaid: bool
    bookingdates: BookingDates
    additionalneeds: str


class BookingCreateRes(BaseModel):
    bookingid: int
    booking: BookingCreateReq
