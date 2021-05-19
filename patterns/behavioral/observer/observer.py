from abc import ABC, abstractmethod
from random import randrange


class Subject(ABC):
    @abstractmethod
    def subscribe(self, observer: 'Observer') -> None:
        pass

    @abstractmethod
    def unsubscribe(self, observer: 'Observer') -> None:
        pass

    @abstractmethod
    def notify(self) -> None:
        pass


class DayPartPublisher(Subject):

    parts = {
        0: 'night',
        1: 'morning',
        2: 'noon',
        3: 'afternoon',
        4: 'evening'
    }

    _state: int = None

    _observers: list['Observer'] = []

    def subscribe(self, observer: 'Observer') -> None:
        print("DayPartPublisher: observer subscribed.")
        self._observers.append(observer)

    def unsubscribe(self, observer: 'Observer') -> None:
        print("DayPartPublisher: observer unsubscribed.")
        self._observers.remove(observer)

    def notify(self) -> None:

        print("DayPartPublisher: Notifying observers...")
        for observer in self._observers:
            observer.update(self._state)

    def change_part(self) -> None:

        print("\nDayPartPublisher:Changing day part.")
        self._state = self._state + 1 if self._state is not None and self._state < 4 else 0

        print(f"DayPartPublisher: Current day part is: {self.parts[self._state]}")
        self.notify()


class Observer(ABC):

    @abstractmethod
    def update(self, state: int) -> None:
        pass


class FirstShiftObserver(Observer):
    def update(self, state: int) -> None:
        if state < 3:
            print(f"{self.__class__.__name__}: Do job at first shift")


class SecondShiftObserver(Observer):
    def update(self, state: int) -> None:
        if state >= 2:
            print(f"{self.__class__.__name__}: Do job at second shift")


if __name__ == "__main__":

    subject = DayPartPublisher()

    observer_a = FirstShiftObserver()
    subject.subscribe(observer_a)

    observer_b = SecondShiftObserver()
    subject.subscribe(observer_b)

    subject.change_part()
    subject.change_part()

    subject.unsubscribe(observer_a)

    subject.change_part()
    subject.change_part()
    subject.change_part()
    subject.change_part()
