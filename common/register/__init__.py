import abc


class ServiceRegister:
    @abc.abstractmethod
    def register(self, name, service_id, address, port, tags):
        pass

    @abc.abstractmethod
    def deregister(self,id):
        pass

    @abc.abstractmethod
    def get(self):
        pass

    @abc.abstractmethod
    def filter(self,name):
        pass