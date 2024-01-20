from pydantic import BaseModel, Field, ConfigDict, RootModel


class Booking(BaseModel):
    booking_id: int = Field(alias='bookingid')

    model_config = ConfigDict(
        populate_by_name=True,
        from_attributes=True
    )


class BookingListRes(RootModel):
    root: list[Booking]


class BookingDates(BaseModel):
    checkin: str
    checkout: str


class BookingCreateReq(BaseModel):
    firstname: str
    lastname: str
    total_price: int = Field(alias='totalprice')
    deposit_paid: bool = Field(alias='depositpaid')
    booking_dates: BookingDates = Field(alias='bookingdates')
    additional_needs: str = Field(alias='additionalneeds')

    model_config = ConfigDict(
        populate_by_name=True,
        from_attributes=True
    )


class BookingCreateRes(BaseModel):
    booking_id: int = Field(alias='bookingid')
    booking: BookingCreateReq

    model_config = ConfigDict(
        populate_by_name=True,
        from_attributes=True
    )
