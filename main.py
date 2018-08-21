import sys
import socket
# from web.server import Server
# from web.mywsgi import Application


class Socket:
    def __init__(self, sock=None):
        if sock is None:
            self.sock = None
        else:
            self.sock = sock

    def get_client(self):
        return self.sock.accept()

    def start(self, host, port):
        self.sock.bind((host, port))
        self.sock.listen()
        print(f"Server started to listen port: {port }...")

    def get_request(self):
        return self.sock.recv(1024).split(b"\r")

    def start_response(self, status, headers):
        response = HttpResponse(status, headers).get_byte_response()
        self.sock.sendall(response)

    def get_start_response(self):
        return self.start_response


class HttpResponse:
    def __init__(self, status, headers, content=""):
        self.status = status
        self.headers = headers
        self.content = content

    def get_byte_response(self):
        response = f"{self.status}"
        for header_key, header_val in self.headers:
            response += "\n" + f"{header_key}: {header_val}"
        response += "\n\n" + self.content
        return response.encode("utf8")


class WebApplication:
    def __init__(self):
        pass

    def __call__(self, request, start_response):
        status = "HTTP/1.1 200 OK"
        headers = [('Content-Type', 'text/plain')]
        start_response(status, headers)
        return b"Hello world!"


class Server:
    def __init__(self, app):
        self.app = app
        self.server_socket = Socket(socket.socket(socket.AF_INET, socket.SOCK_STREAM))

    def run(self):
        host = "127.0.0.1"
        port = int(sys.argv[1])
        self.server_socket.start(host, port)

        while True:
            client, address = self.server_socket.get_client()
            client = Socket(client)

            start_response = client.get_start_response()
            request = client.get_request()
            print("Request: ", request)

            response = self.app(request, start_response)
            client.sock.sendall(response)
            client.sock.close()


def main():
    app = WebApplication()
    server = Server(app )
    server.run()


if __name__ == "__main__":
    main()