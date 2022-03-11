from common.register import ServiceRegister
import consul


class ConsulRegister(ServiceRegister):

    def __init__(self, host, port):
        self.c = consul.Consul(host=host, port=port)

    def register(self, name, service_id, address, port, tags):
        check = {
            "Name": name,
            "GRPC": f"{address}:{port}",
            "Interval": "5s",
            "Timeout": "5s",
            "Method": "get",
            "DeregisterCriticalServiceAfter": "5s"
        }
        return self.c.agent.service.register(
            name=name,
            service_id=service_id,
            address=address,
            port=port,
            tags=tags,
            check=check
        )

    def deregister(self, id):
        return self.c.agent.service.deregister(id)

    def get(self):
        return self.c.agent.services()

    def filter(self,name):
        pass
