from collections.abc import Iterable, Iterator
from  typing import Any


class AlphabeticalOrderIterator(Iterator):
    _position: int = None
    _reverse: bool = False

    def __init__(self, collection: 'WordsCollection', *, reverse: bool = False) -> None:
        self._collection = collection
        self._reverse = reverse
        self._position = -1 if reverse else 0

    def __next__(self):
        try:
            value = self._collection[self._position]
            self._position += -1 if self._reverse else 1
        except IndexError:
            raise StopIteration()
        return value


class WordsCollection(Iterable):
    def __init__(self, collection: list[Any] = []) -> None:
        self._collection = collection

    def __iter__(self) -> AlphabeticalOrderIterator:
        return AlphabeticalOrderIterator(self._collection)

    def get_reverse_iterator(self) -> AlphabeticalOrderIterator:
        return AlphabeticalOrderIterator(self._collection, reverse=True)

    def add(self, item: Any):
        self._collection.append(item)


if __name__ == '__main__':
    words_collection = WordsCollection()
    words_collection.add('First')
    words_collection.add("Second")
    words_collection.add("Third")

    print('\n'.join(words_collection))
    print('\n'.join(words_collection.get_reverse_iterator()))
