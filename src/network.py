import socket
import json


class Network:
    """
    Represents a network connection to a server.

    Attributes:
        host (str): The host address of the server.
        port (int): The port number of the server.
        s (socket.socket): The socket object for the network connection.
    """

    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def start(self):
        """
        Connects to the specified host and port, receives data from the server,
        and writes it to "config.json" file.
        """
        self.s.connect((self.host, self.port))
        data = self.s.recv(1024).decode("ascii").replace("'", "\"")
        with open(r"..\config.json", "w") as jsonFile:
            jsonFile.write(data)

    def send_data(self, keys):
        """
        Sends the specified keys as JSON data to the server.

        Args:
            keys (list): A list of keys to send.

        Raises:
            TypeError: If the keys parameter is not a list.
        """
        if not isinstance(keys, list):
            raise TypeError("keys must be a list")
        self.s.sendall(str(json.dumps({"keys": keys, "dead": False})).encode('ascii'))

    def get_data(self):
        """
        Receives data from the server and returns it as a Python dictionary.

        Returns:
            dict: The received data as a dictionary.
        """
        return json.loads(self.s.recv(1024).decode("ascii"))
