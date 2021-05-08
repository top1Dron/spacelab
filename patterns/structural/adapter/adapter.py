class ClientInterface:
    def current_realization(self):
        print('Current realization')


class NewLibrary:
    def new_functionality(self):
        print('New function')


class NewLibraryAdapter(ClientInterface):
    '''
    Adapt new_functionality from new library
    to usage in client interface
    '''
    def __init__(self, library: NewLibrary):
        self._library = library

    def current_realization(self):
        super().current_realization()
        self._library.new_functionality()


def client_code(client: ClientInterface):
    client.current_realization()


if __name__ == '__main__':
    library = NewLibrary()
    client_code(NewLibraryAdapter(library))
