from abc import ABC, abstractmethod


class Observer(ABC):
    @abstractmethod
    def update(self, msg):
        pass


class SmsNotification(Observer):
    def update(self, msg):
        print(msg)
