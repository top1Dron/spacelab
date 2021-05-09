class Service1:
    def execute(self):
        print('Service 1 execution')


class Service2:
    def execute(self):
        print('Service 2 execution')


class Service3:
    def execute(self):
        print('Service 3 execution')


class Service4:
    def execute(self):
        print('Service 4 execution')


class Facade:
    def __init__(self):
        self._service1 = Service1()
        self._service2 = Service2()
        self._service3 = Service3()
        self._service4 = Service4()

    def execute(self):
        print('Start of services execution')
        self._service1.execute()
        self._service3.execute()
        self._service2.execute()
        self._service4.execute()
        print('End of services execution')


if __name__ == '__main__':
    Facade().execute()
