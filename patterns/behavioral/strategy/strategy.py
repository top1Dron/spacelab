from abc import ABC, abstractmethod
from datetime import datetime as dt


class Executer:
    _algorithm: 'Algorithm' = None

    @property
    def algorithm(self) -> 'Algorithm':
        return self._algorithm

    @algorithm.setter
    def algorithm(self, algorithm):
        self._algorithm = algorithm

    def do_something(self):
        self.algorithm.execute()


class Algorithm(ABC):
    @abstractmethod
    def execute(self):
        pass


class Algorithm1(Algorithm):

    def execute(self):
        print('Do something applying 1 algorithm')


class Algorithm2(Algorithm):

    def execute(self):
        print('Do something applying 2 algorithm')


if __name__ == '__main__':
    executer = Executer()
    executer.algorithm = Algorithm1() if dt.now().minute & 1 else Algorithm2()
    executer.do_something()
