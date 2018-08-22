import sys
import socket
from web.http import HttpRequest, HttpResponse


class Socket:
    def __init__(self, sock=None):
        if sock is None:
            self.sock = None
        else:
            self.sock = sock

    def get_client_and_address(self):
        return self.sock.accept()

    def start(self, host, port):
        self.sock.bind((host, port))
        self.sock.listen()
        print(f"Server started to listen port: {port }...")

    def get_request(self):
        r = self.sock.recv(1024)
        return HttpRequest(r.split(b"\r"))

    def start_response(self, status, headers):
        response = HttpResponse(status, headers).get_byte_response()
        print(type(response), response)
        self.sock.sendall(response)

    def get_start_response(self):
        return self.start_response


class Server:
    def __init__(self, app):
        self.app = app
        self.server_socket = Socket(socket.socket(socket.AF_INET, socket.SOCK_STREAM))

    def run(self):
        host = "127.0.0.1"
        port = int(sys.argv[1])
        self.server_socket.start(host, port)

        while True:
            client, address = self.server_socket.get_client_and_address()
            client = Socket(client)

            start_response = client.get_start_response()
            request = client.get_request()
            response = self.app(request, start_response)
            print(response)
            if not response:
                break
            client.sock.sendall(response)
            client.sock.close()