from threading import Lock


class SingletonMeta(type):
    _instance = None

    _lock: Lock = Lock()

    def __call__(cls, *args, **kwargs):
        with cls._lock:
            if not cls._instance:
                cls._instance = super().__call__(*args, **kwargs)
        return cls._instance


class Singleton(metaclass=SingletonMeta):

    def some_logic(self):
        pass


# class SingletonWithDict:
#
#     def some_logic(self):
#         pass
#
#     __data = {
#         'name': None
#     }
#
#     def __init__(self, kwargs: dict = None):
#         self.__dict__ = SingletonWithDict.__data
#         for arg in kwargs:
#             self.__dict__[arg] = kwargs[arg]


# if __name__ == '__main__':
#     print(id(Singleton()), id(Singleton()), id(Singleton()), id(Singleton()), id(Singleton()), sep='\n')

    # inst1 = SingletonWithDict(dict(age=3, name='Inst1', instance_number=1))
    # inst2 = SingletonWithDict(dict(age=10, name='Inst2', instance_number=2))
    # print(inst1.__dict__, inst2.__dict__, sep='\n')
    # print(id(inst1), id(inst2), sep='\n')
    # print(inst1.age)
