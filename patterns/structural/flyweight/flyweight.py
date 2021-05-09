class TreeType:
    def __init__(self, name: str, color: str, texture: str):
        self.__name = name
        self.__color = color
        self.__texture = texture

    def draw(self, canvas: str, x: int, y: int):
        print(f'Draw {self.__name} with texture {self.__texture} at position({x}, {y}) with canvas: {canvas}')


class TreeFactory:
    tree_types: dict[TreeType] = {}

    @classmethod
    def get_tree_type(cls, name: str, color: str, texture) -> TreeType:
        if not cls.tree_types.get((name, color, texture)):
            cls.tree_types[(name, color, texture)] = TreeType(name, color, texture)
        return cls.tree_types[(name, color, texture)]


class Tree:
    def __init__(self, x, y, name: str, color: str, texture):
        self.__x = x
        self.__y = y
        self.__tree_type = TreeFactory.get_tree_type(name, color, texture)

    def draw(self, canvas: str):
        self.__tree_type.draw(canvas, self.__x, self.__y)


class Forest:
    def __init__(self):
        self.__trees: list[Tree] = []

    def plantTree(self, x: int, y: int, name: str, color: str, texture: str) -> None:
        tree = Tree(x, y, name, color, texture)
        self.__trees.append(tree)

    def draw(self, canvas: str) -> None:
        for tree in self.__trees:
            tree.draw(canvas)


if __name__ == '__main__':
    forest = Forest()
    forest.plantTree(x=0, y=0, name='Oak', color='brown', texture='texture1')
    forest.plantTree(x=3, y=2, name='Oak', color='brown', texture='texture1')
    forest.plantTree(x=4, y=4, name='Maple', color='brown', texture='texture2')
    forest.draw('canvas1')
