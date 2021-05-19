from abc import ABC, abstractmethod


class Component(ABC):

    @abstractmethod
    def accept(self, visitor: 'Visitor') -> None:
        pass


class Disassembler(Component):

    def accept(self, visitor: 'Visitor') -> None:
        visitor.use_disassembler(self)

    def disassemble(self) -> str:
        return "Make disassembly"


class Collector(Component):

    def accept(self, visitor: 'Visitor'):
        visitor.use_collector(self)

    def collect(self) -> str:
        return "Make assembly"


class Visitor(ABC):

    @abstractmethod
    def use_disassembler(self, component: Disassembler) -> None:
        pass

    @abstractmethod
    def use_collector(self, component: Collector) -> None:
        pass


class ConcreteVisitor(Visitor):
    def use_disassembler(self, component) -> None:
        print(f"{component.disassemble()} using Disassembler")

    def use_collector(self, component) -> None:
        print(f"{component.collect()} using Collector")


if __name__ == "__main__":
    components = [Disassembler(), Collector()]

    visitor = ConcreteVisitor()
    for component in components:
        component.accept(visitor)
