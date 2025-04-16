from abc import abstractmethod, ABC


class Show:
    def __init__(self, st_time, ed_time, hall, movie):
        self.st = st_time
        self.ed = ed_time
        self.hall = hall
        self.movie = movie
        self.slots = []
        self.is_scheduled = False
        self.schedule_show()

    def create_slot(self, seat):
        seats = self.get_seats()
        if seat not in seats:
            return None

        slot = Slot(seat)
        self.slots.append(slot)
        return slot

    def get_seats(self):
        return self.hall.get_seats()

    def schedule_show(self):
        self.is_scheduled = self.hall.schedule_show(self)
        if not self.is_scheduled:
            raise Exception("Can not schedule the show")

    def show_seating(self):
        return self.slots

    def is_self_slots(self, slots):
        slots_to_book = 0
        for show_slot in self.slots:
            for slot in slots:
                if show_slot == slot:
                    slots_to_book += 1

        if slots_to_book != len(slots):
            print("Slot Undefined")
            return False

        return True

    def book_slots(self, slots):
        is_self_slots = self.is_self_slots(slots)
        if not is_self_slots:
            return False

        for slot in slots:
            slot.book_slot()

        return True

    def cancel_slots(self, slots):
        is_self_slots = self.is_self_slots(slots)
        if not is_self_slots:
            return False

        for slot in slots:
            slot.cancel_slot()
            slot.free_slot()

        return True

    def get_slots_price(self, slots):
        is_self_slots = self.is_self_slots(slots)
        if not is_self_slots:
            return None

        final_amount = 0
        for slot in slots:
            final_amount += slot.seat.price

        return final_amount

    def __repr__(self):
        return self.__dict__.__str__()


class Slot:
    def __init__(self, seat):
        self.seat = seat
        self.status = SlotAvailable()

    def free_slot(self):
        self.status = self.status.free_slot()

    def book_slot(self):
        self.status = self.status.book_slot()

    def cancel_slot(self):
        self.status = self.status.cancel_slot()

    def __repr__(self):
        return f"({self.seat.seat_no} - {self.status})"


class SlotStatus(ABC):

    @abstractmethod
    def free_slot(self):
        pass
    
    @abstractmethod
    def book_slot(self):
        pass

    @abstractmethod
    def cancel_slot(self):
        pass

    def __repr__(self):
        return self.__class__.__name__


class SlotAvailable(SlotStatus):

    def free_slot(self):
        print("Already Free")
        return self

    def cancel_slot(self):
        raise Exception("Slot is Available")

    def book_slot(self):
        return SlotBooked()
    
    
class SlotBooked(SlotStatus):
    def free_slot(self):
        raise Exception("Can not free a booked slot")

    def cancel_slot(self):
        return SlotCancelled()

    def book_slot(self):
        print("Slot is already booked")
    

class SlotCancelled(SlotStatus):
    def free_slot(self):
        return SlotAvailable()

    def book_slot(self):
        raise Exception("Cannot book after cancellation")

    def cancel_slot(self):
        print("Already cancelled")
