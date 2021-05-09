from abc import ABC, abstractmethod


class HardServiceInterface(ABC):

    @abstractmethod
    def execute(self):
        pass


class HardService(HardServiceInterface):

    def execute(self):
        print('Hard service execution')


class ServiceOptimizer(HardServiceInterface):
    def __init__(self, service: HardService):
        self._service = service

    def execute(self):
        if self.__check_access():
            self.__start_connection_with_service()
            self.__optimize_execution()
            self._service.execute()
            self.__close_connection_with_service()

    def __start_connection_with_service(self):
        print('Connecting with hard service')

    def __check_access(self):
        print('Checking for user access for service')
        print('Access is allowed')
        return True


    def __optimize_execution(self):
        print('Preparation before service execution, optimizing system')

    def __close_connection_with_service(self):
        print('Closing connection with service')


if __name__ == '__main__':
    service = ServiceOptimizer(HardService())
    service.execute()
