from booking import BookingTicket, Booked
from payment import CashPayment


class BookingSystem:
    def __init__(self):
        self.bookings = []

    def book(self, booking_no, show, slots, payment_type=CashPayment()):
        print(f"Booking for {booking_no}")
        amount = show.get_slots_price(slots)
        booking_ticket = BookingTicket(booking_no, show, slots, amount, payment_type)
        self.bookings.append(booking_ticket)

        payment_status = payment_type.process_payment(amount)
        if payment_status:
            booking_ticket.book_slots()

        return booking_ticket

    @staticmethod
    def show_seating(show):
        print(show.show_seating())

    def cancel_booking(self, booking_ticket):
        print(f"Cancelling Booking - {booking_ticket.booking_no}")

        if booking_ticket not in self.bookings:
            raise Exception("Booking Not Found")

        booking_ticket.cancel_booking()
        is_refundable = booking_ticket.is_refundable
        if is_refundable:
            self.process_refund(booking_ticket)

    @staticmethod
    def process_refund(booking_ticket):
        booking_amount = booking_ticket.get_booking_amount()

        payment_type = booking_ticket.get_payment_type()
        payment_type.process_payment(booking_amount)

        booking_ticket.refund_booking()

