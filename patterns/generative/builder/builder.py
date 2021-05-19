from abc import ABCMeta, abstractmethod
from typing import  Any


class Builder(metaclass=ABCMeta):

    def __init__(self):
        self.reset()

    def reset(self) -> 'Product':
        self._product = Product()

    @property
    def product(self):
        return self._product

    @abstractmethod
    def add_first_element(self):
        pass

    @abstractmethod
    def add_second_element(self):
        pass

    @abstractmethod
    def add_third_element(self):
        pass


class ConcreteBuilder1(Builder):

    def add_first_element(self):
        self._product.add('Part1-CB1')
        return self

    def add_second_element(self):
        self._product.add('Part2-CB1')
        return self

    def add_third_element(self):
        self._product.add('Part3-CB1')
        return self


class ConcreteBuilder2(Builder):

    def add_first_element(self):
        self._product.add('Part1-CB2')
        return self

    def add_second_element(self):
        self._product.add('Part2-CB2')
        return self

    def add_third_element(self):
        self._product.add('Part3-CB2')
        return self


class Product:
    def __init__(self):
        self._parts = []

    def add(self, part: Any) -> None:
        self._parts.append(part)

    @property
    def parts(self):
        return f"Product parts: {', '.join(self._parts)}"


class Director:
    def __init__(self, builder: Builder):
        self.__builder = builder

    def build_first_obj(self):
        return self.__builder.add_first_element().add_second_element()

    def build_second_obj(self):
        return self.__builder.add_second_element().add_third_element()


if __name__ == '__main__':
    builder1 = ConcreteBuilder1()
    director = Director(builder1)
    director.build_first_obj()
    print(builder1.product.parts)

    builder2 = ConcreteBuilder2()
    director = Director(builder2)
    director.build_second_obj()
    print(builder2.product.parts)
