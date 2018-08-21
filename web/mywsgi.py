# class Application:
#     """ the role of this class is to process an HTTP Request and return an HTTP Response"""
#     def __init__(self):
#         pass
#
#     def __call__(self, request, start_response):
#         status = "200 OK"
#         response_headers = [('Content-type', 'text/plain')]
#         start_response(status, response_headers)
#         return "Hello World!\n"