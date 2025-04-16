from abc import ABC, abstractmethod


class Payment(ABC):

    @abstractmethod
    def process_payment(self, amount):
        pass


class CashPayment(Payment):
    def process_payment(self, amount):
        print("Payment is processed via Cash")
        return True


class CardPayment(Payment):
    def process_payment(self, amount):
        print("Payment is processed via Card")
        return True
