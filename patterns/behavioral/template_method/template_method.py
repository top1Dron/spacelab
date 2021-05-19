from abc import ABC, abstractmethod


class Executer(ABC):
    def template_method(self) -> None:

        self.base_operation1()
        self.required_operations1()
        self.base_operation2()
        self.hook1()
        self.required_operations2()
        self.base_operation3()
        self.hook2()

    def base_operation1(self) -> None:
        print("Executer says: I am doing the bulk of the work")

    def base_operation2(self) -> None:
        print("Executer says: But I let subclasses override some operations")

    def base_operation3(self) -> None:
        print("Executer says: But I am doing the bulk of the work anyway")

    @abstractmethod
    def required_operations1(self) -> None:
        pass

    @abstractmethod
    def required_operations2(self) -> None:
        pass

    def hook1(self) -> None:
        pass

    def hook2(self) -> None:
        pass


class SimplifiedExecuter(Executer):
    def required_operations1(self) -> None:
        print("SimplifiedExecuter says: Implemented Operation1")

    def required_operations2(self) -> None:
        print("SimplifiedExecuter says: Implemented Operation2")


class ExtendedExecuter(Executer):
    def required_operations1(self) -> None:
        print("ExtendedExecuter says: Implemented Operation1")

    def required_operations2(self) -> None:
        print("ExtendedExecuter says: Implemented Operation2")

    def hook1(self) -> None:
        print("ExtendedExecuter says: Overridden Hook1")

    def hook2(self) -> None:
        print("ExtendedExecuter says: Overridden Hook2")


def client_code(abstract_class: Executer) -> None:

    # ...
    abstract_class.template_method()
    # ...


if __name__ == "__main__":
    client_code(SimplifiedExecuter())
    print()
    client_code(ExtendedExecuter())
