from abc import ABCMeta, abstractmethod


class TriangleDoesNotExistError(Exception):
    pass


class Cloneable(metaclass=ABCMeta):

    @abstractmethod
    def copy(self):
        pass


class Shape(Cloneable, metaclass=ABCMeta):
    pass


class Triangle(Shape):

    def __init__(self, first_side: float, second_side: float, third_side: float) -> None:
        if Triangle.validate(first_side, second_side, third_side):
            self.__third_side = third_side
            self.__first_side = first_side
            self.__second_side = second_side
        else:
            raise TriangleDoesNotExistError("Треугольник не существует")

    @classmethod
    def validate(cls, first_side: float, second_side: float, third_side: float) -> bool:
        if (first_side + second_side <= third_side or
                first_side + third_side <= second_side or
                second_side + third_side <= first_side):
            return False
        return True

    def copy(self):
        return Triangle(first_side=self.__first_side,
                        second_side=self.__second_side,
                        third_side=self.__third_side)


class Rectangle(Cloneable):

    def __init__(self, height: float, width: float):
        self.__height = height
        self.__width = width
        self.square = self.__width * self.__height

    def set_verticies_name(self, name: str) -> None:
        self.__verticies_name = name

    @property
    def square(self):
        return self.__square

    @square.setter
    def square(self, value):
        self.__square = value

    def copy(self):
        copied_rect = Rectangle(self.__height, self.__width)
        if hasattr(self, '_Rectangle__verticies_name'):
            copied_rect.set_verticies_name(self.__verticies_name)
        return copied_rect


if __name__ == '__main__':
    triangle = Triangle(10, 30, 25)
    copied_triangle = triangle.copy()
    print(triangle.__dict__, copied_triangle.__dict__, sep='\n')

    print('-' * 100)

    rectangle = Rectangle(20, 25)
    # rectangle.set_verticies_name('ABCD')
    copied_triangle = rectangle.copy()
    print(rectangle.__dict__, copied_triangle.__dict__, sep='\n')
