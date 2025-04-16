from abc import ABC, abstractmethod


class BookingTicket:
    def __init__(self, booking_no, show, slots, amount, payment_type, is_refundable=True):
        self.booking_no = booking_no
        self.show = show
        self.slots = slots
        self.amount = amount
        self.payment_type = payment_type
        self.is_refundable = is_refundable
        self.booking_status = Initiate()

    def book_slots(self):
        status = self.show.book_slots(self.slots)
        if status:
            self.booking_status = self.booking_status.book()

    def cancel_booking(self):
        status = self.show.cancel_slots(self.slots)
        if status:
            self.booking_status = self.booking_status.cancel()

    def refund_booking(self):
        self.booking_status = self.booking_status.refund()

    def get_status(self):
        return self.booking_status

    def get_booking_amount(self):
        return self.amount

    def get_payment_type(self):
        return self.payment_type

    def __repr__(self):
        return self.__dict__.__str__()


class BookingStatus(ABC):

    @abstractmethod
    def book(self):
        pass

    @abstractmethod
    def cancel(self):
        pass

    @abstractmethod
    def refund(self):
        pass


class Initiate(BookingStatus):
    def book(self):
        return Booked()

    def cancel(self):
        print("Can't cancel as no booking done")
        return self

    def refund(self):
        print("Can't refund as no booking done")
        return self


class Booked(BookingStatus):
    def book(self):
        print("Already booked")
        return self

    def cancel(self):
        return Cancelled()

    def refund(self):
        raise Exception("No refund on booked tickets")


class Cancelled(BookingStatus):
    def book(self):
        raise Exception("Tkt is cancelled")

    def cancel(self):
        print("Already cancelled")
        return self

    def refund(self):
        return Refund()


class Refund(BookingStatus):
    def book(self):
        raise Exception("Can't book now")

    def cancel(self):
        raise Exception("Can't cancel now")

    def refund(self):
        print("Already refund")
        return self
