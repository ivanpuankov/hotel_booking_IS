"""Система бронирования отелей — точка входа в приложение."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import date
from typing import Dict, List


@dataclass
class Booking:
    """Бронирование номера."""

    booking_id: int
    guest_name: str
    room_number: str
    check_in: date
    check_out: date
    status: str = "active"


class BookingService:
    """Сервис управления бронированиями."""

    def __init__(self) -> None:
        self._bookings: Dict[int, Booking] = {}
        self._next_id = 1

    def create_booking(
        self,
        guest_name: str,
        room_number: str,
        check_in: date,
        check_out: date,
    ) -> Booking:
        """Создаёт новое бронирование с валидацией данных гостя."""
        if not guest_name.strip():
            raise ValueError("ФИО гостя обязательно для заполнения")
        if check_out <= check_in:
            raise ValueError("Дата выезда должна быть позже даты заезда")

        booking = Booking(
            booking_id=self._next_id,
            guest_name=guest_name,
            room_number=room_number,
            check_in=check_in,
            check_out=check_out,
        )
        self._bookings[booking.booking_id] = booking
        self._next_id += 1
        return booking

    def cancel_booking(self, booking_id: int) -> None:
        """Отменяет бронирование по идентификатору."""
        booking = self._bookings.get(booking_id)
        if booking is None:
            raise KeyError(f"Бронирование {booking_id} не найдено")
        booking.status = "cancelled"

    def list_bookings(self) -> List[Booking]:
        """Возвращает список активных бронирований."""
        return [b for b in self._bookings.values() if b.status == "active"]


def main() -> None:
    """Точка входа в приложение."""
    print("Hotel Booking System started")


if __name__ == "__main__":
    main()
