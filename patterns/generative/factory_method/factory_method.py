from abc import ABCMeta, abstractmethod
from datetime import datetime as dt


class Shape(metaclass=ABCMeta):

    @abstractmethod
    def get_square(self):
        pass


class Quadrate(Shape):

    @property
    def side(self):
        return self.__side

    @side.setter
    def side(self, value: float):
        self.__side = value

    def get_square(self) -> float:
        return self.side * self.side


class Rectangle(Shape):

    @property
    def length(self):
        return self.__length

    @length.setter
    def length(self, value: float):
        self.__length = value

    @property
    def width(self):
        return self.__side

    @width.setter
    def width(self, value: float):
        self.__width = value

    def get_square(self) -> float:
        return self.__width * self.__length


class ShapeFactory(metaclass=ABCMeta):

    @abstractmethod
    def factory_method(self):
        pass


class QuadrateFactory(ShapeFactory):

    def factory_method(self):
        return Quadrate()


class RectangleFactory(ShapeFactory):

    def factory_method(self):
        return Rectangle()


if __name__ == '__main__':
    shapes = QuadrateFactory()
    if dt.now().minute & 1:
        factory = QuadrateFactory()
    else:
        factory = RectangleFactory()

    print(factory.factory_method())


