import socket
import sys


class Server:
    """
    Represents a server that handles multiple clients for this game.

    Attributes:
        port (int): The port number on which the server will listen for incoming connections.
        conf (tuple): The server configuration consisting of the IP address and port number.
        s (socket.socket): The server socket object.
        number_of_clients (int): The maximum number of clients that the server can handle.
        clients (list): The list of connected clients.

    Methods:
        __init__(self, number_of_clients, port): Initializes a Server object.
    """

    def __init__(self, number_of_clients, port):
        """
        Initializes a Server object.

        Args:
            number_of_clients (int): The maximum number of clients that the server can handle.
            port (int): The port number on which the server will listen for incoming connections.
        """
        self.port = port
        self.conf = ('', self.port)
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.bind(self.conf)
        self.number_of_clients = number_of_clients
        self.clients = []


if __name__ == '__main__':
    server = Server(int(sys.argv[1]), 5050)
