from datetime import datetime as dt


class Calculator:
    _state: float = 0

    def __add__(self, other: float):
        self._state += other
        return self._state

    def __mul__(self, other: float):
        self._state *= other
        return self._state

    def __truediv__(self, other):
        self._state //= other
        return self._state

    def __floordiv__(self, other):
        self._state /= other
        return self._state

    def __sub__(self, other):
        self._state -= other
        return self._state

    def __str__(self):
        return self._state

    def save(self) -> 'Memento':
        return Memento(self._state)

    def restore(self, memento: 'Memento'):
        self._state = memento.state


class Memento:
    def __init__(self, state: float):
        self._state = state
        self._date = str(dt.now())[:19]

    @property
    def state(self):
        return self._state

    @property
    def date(self):
        return self._date


class StateHistory:
    def __init__(self, calc: Calculator):
        self._mementos: list[Memento] = list()
        self._calculator = calc

    def backup(self):
        print('Saving calculator state at ', end='')
        self._mementos.append(self._calculator.save())
        print(self._mementos[-1].date)

    def undo(self) -> None:
        if not len(self._mementos):
            return
        memento = self._mementos.pop()
        print(f'Start restoring calculator state to {memento.state}')
        try:
            self._calculator.restore(memento)
        except Exception:
            self.undo()

    def show_history(self):
        print(f'History of states:')
        for memento in self._mementos:
            print(f'{memento.date}: {memento.state}')


if __name__ == '__main__':
    calculator = Calculator()
    history = StateHistory(calculator)

    history.backup()
    calculator + 5

    history.backup()
    calculator * 2

    history.backup()
    calculator // 3

    history.backup()
    calculator - 1

    history.backup()
    calculator / 2

    print()
    history.show_history()
    print('Rollback to previous state')
    history.undo()

    print('One more rollback')
    history.undo()
