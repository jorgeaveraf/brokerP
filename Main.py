from Broker import Broker, EchoService
from Client import Client

def main():
    # Create a Broker
    broker = Broker()

    # Create and register services
    echo_service = EchoService()
    broker.register_service('echo', echo_service)

    # Create a Client
    client = Client(broker)

    # Make requests
    client.make_request('echo', 'Hello, World!')
    client.make_request('echo', 'Another request')
    client.make_request('nonexistent', 'This should fail')

if __name__ == "__main__":
    main()
