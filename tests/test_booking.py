"""Тесты создания и отмены бронирования."""

from datetime import date

import pytest

from src.main import BookingService


@pytest.fixture()
def service() -> BookingService:
    return BookingService()


def test_create_booking(service: BookingService) -> None:
    booking = service.create_booking(
        "Петров Пётр", "101", date(2026, 12, 1), date(2026, 12, 5)
    )

    assert booking.booking_id == 1
    assert booking.status == "active"
    assert len(service.list_bookings()) == 1


def test_create_booking_invalid_dates(service: BookingService) -> None:
    with pytest.raises(ValueError):
        service.create_booking(
            "Петров Пётр", "101", date(2026, 12, 5), date(2026, 12, 1)
        )


def test_cancel_booking(service: BookingService) -> None:
    booking = service.create_booking(
        "Петров Пётр", "101", date(2026, 12, 1), date(2026, 12, 5)
    )
    service.cancel_booking(booking.booking_id)

    assert booking.status == "cancelled"
    assert service.list_bookings() == []


def test_cancel_unknown_booking(service: BookingService) -> None:
    with pytest.raises(KeyError):
        service.cancel_booking(42)
