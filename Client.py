class Client:
    def __init__(self, broker):
        self.broker = broker

    def make_request(self, service_name, request):
        response = self.broker.send_request(service_name, request)
        print(f"Response from {service_name}: {response}")
