from abc import ABC, abstractmethod
from datetime import datetime as dt


class AbstractProductA(ABC):

    @abstractmethod
    def some_logic(self):
        pass


class AbstractProductB(ABC):

    @abstractmethod
    def some_logic(self):
        pass


class ConcreteProductA1(AbstractProductA):

    def some_logic(self):
        print('Some logic of product A1')


class ConcreteProductA2(AbstractProductA):

    def some_logic(self):
        print('Some logic of product A2')


class ConcreteProductB1(AbstractProductB):

    def some_logic(self):
        print('Some logic of product B1')


class ConcreteProductB2(AbstractProductB):
    def some_logic(self):
        print('Some logic of product B2')


class AbstractFactory(ABC):

    @abstractmethod
    def create_product_a(self) -> AbstractProductA:
        pass

    @abstractmethod
    def create_product_b(self) -> AbstractProductB:
        pass


class ConcreteFactory1(AbstractFactory):

    def create_product_a(self) -> AbstractProductA:
        return ConcreteProductA1()

    def create_product_b(self) -> AbstractProductB:
        return ConcreteProductB1()


class ConcreteFactory2(AbstractFactory):

    def create_product_a(self) -> AbstractProductA:
        return ConcreteProductA2()

    def create_product_b(self) -> AbstractProductB:
        return ConcreteProductB2()


if __name__ == '__main__':
    if dt.now().minute & 1:
        factory = ConcreteFactory2()
    else:
        factory = ConcreteFactory1()

    product_a = factory.create_product_a()
    product_b = factory.create_product_b()
    product_a.some_logic()
    product_b.some_logic()
