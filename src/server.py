import json
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
        wait_for_clients(self): Waits for clients to connect to the server.
        start(self): Starts the server and initializes the game configuration for each client.
        main(self): The main method that runs the server.
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

    def wait_for_clients(self):
        """
        Waits for clients to connect to the server.

        This method listens for incoming client connections and accepts them up to the specified number of clients.
        The accepted clients are stored in the `clients` list.

        Raises:
            Any exception that occurs during the process is silently ignored.
        """
        try:
            self.s.listen(10)

            for i in range(self.number_of_clients):
                c, addr = self.s.accept()
                self.clients.append((c, addr))

            self.s.close()

        except:
            pass

    def start(self):
        """
        Starts the server and initializes the game configuration for each client.

        The function waits for clients to connect and then sends the game configuration
        to each client.
        """
        self.wait_for_clients()

        config = {
            "cell_size": 30,
            "back_color": [255, 255, 255],
            "fruit_color": [255, 0, 0],
            "block_color": [139, 69, 19],
            "block_cells": [
                [14, 14],
                [13, 14],
                [12, 14],
                [15, 14],
            ],
            "sx": 30,
            "sy": 50,
            "table_size": 25,
            "height": 1000,
            "width": 800,
            "id": -1,
            "snakes": []
        }

        for i in range(len(self.clients)):
            config['snakes'].append({
                "id": i,
                "keys": {
                    'snake_' + str(i) + '_w': "UP",
                    'snake_' + str(i) + '_s': "DOWN",
                    'snake_' + str(i) + '_a': "LEFT",
                    'snake_' + str(i) + '_d': "RIGHT",
                },
                "sx": 2 * i,
                "sy": 3 * i,
                "color": (12 * (i + 10), 12 * (i * 10), 12),
                "direction": "LEFT",
            })

        for ind, it in enumerate(self.clients):
            config['id'] = ind
            it[0].sendall(str(json.dumps(config)).encode('ascii'))

    def main(self):
        """
        The main method that runs the server.
        """
        self.start()


if __name__ == '__main__':
    server = Server(int(sys.argv[1]), 5050)
    server.main()
