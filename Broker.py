class Broker:
    def __init__(self):
        self.services = {}

    def register_service(self, service_name, service):
        self.services[service_name] = service
        print(f"Service '{service_name}' registered.")

    def send_request(self, service_name, request):
        if service_name in self.services:
            service = self.services[service_name]
            return service.handle_request(request)
        else:
            return f"Service '{service_name}' not found."


class Service:
    def handle_request(self, request):
        pass


class EchoService(Service):
    def handle_request(self, request):
        return f"Echo: {request}"
