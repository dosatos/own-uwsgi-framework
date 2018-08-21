# import sys
#
# import socket
#
#
# class Socket:
#     def __init__(self, host='localhost', port=9005, sock=None):
#         self.host = host
#         self.port = port
#         if sock is None:
#             self.sock = socket.socket((socket.AF_INET, socket.SOCK_STREAM))
#         else:
#             self.sock= sock
#
#     def get_host(self):
#         return self.host
#
#     def set_host(self, host):
#         self.host = host
#
#     def get_port(self):
#         return self.port
#
#     def set_port(self, port):
#         self.port = port
#
#     def bind(self, host=None, port=None):
#         if host is not None:
#             self.set_host(host)
#         if port is not None:
#             self.set_port(port)
#         self.sock.bind((self.host, self.port))
#
#     def accept(self):
#         return self.sock.accept()
#
#     def start_response(self, status, response_headers):
#         self.send('Status: %s\r\n' % status)
#         for header in response_headers:
#             self.send('%s: %s\r\n' % header)
#
#
#
# class Server:
#     def __init__(self, application, host='localhost', port=9005, sock=None):
#         self.application = application
#         self.host = host
#         self.port = port
#         if sock is None:
#             self.sock = Socket()
#         else:
#             self.sock = socket
#
#     def start_listenning(self):
#         self.sock.bind((self.host, self.port))
#         self.sock.listen()
#         print(f"Server is listening at {self.host}:{self.port}...")
#
#     def run(self):
#         self.start_listenning()
#         while True:
#             client_connection, _ = self.sock.accept()
#             request = client_connection.recv(1024)
#             response = self.application(request, self.sock.start_response)
#             for r in response:
#                 client_connection.send(r)
#             client_connection.close()