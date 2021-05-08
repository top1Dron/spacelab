from abc import ABCMeta, abstractmethod


class Builder(metaclass=ABCMeta):

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
        self.__first_element = '1 concrete builder - first element'
        return self

    def add_second_element(self):
        self.__second_element = '1 concrete builder - second element'
        return self

    def add_third_element(self):
        self.__third_element = '1 concrete builder - third element'
        return self


class ConcreteBuilder2(Builder):

    def add_first_element(self):
        self.__first_element = '2 concrete builder - first element'
        return self

    def add_second_element(self):
        self.__second_element = '2 concrete builder - second element'
        return self

    def add_third_element(self):
        self.__third_element = '2 concrete builder - third element'
        return self


class Director:
    def __init__(self, builder: Builder):
        self.__builder = builder

    def build_first_obj(self):
        return self.__builder.add_first_element().add_second_element()

    def build_second_obj(self):
        return self.__builder.add_second_element().add_third_element()


if __name__ == '__main__':
    director = Director(ConcreteBuilder1())
    print(director.build_first_obj().__dict__)

    director = Director(ConcreteBuilder2())
    print(director.build_second_obj().__dict__)
