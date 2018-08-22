import logging
from web.shortcuts import parse_method_resources_http_version


logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(levelname)s %(message)s',
                    filename='/tmp/myapp_debug.log',
                    filemode='w')


class HttpResponse:
    def __init__(self, status, headers, content=""):
        self.status = status
        self.headers = headers
        self.content = content

    def get_byte_response(self):
        response = f"{self.status}"
        for header_key, header_val in self.headers:
            response += "\n" + f"{header_key}: {header_val}"
        response = response.strip() + '\r\n\r\n' + self.content
        print(response)
        return response.encode("utf8")


class HttpRequest:
    def __init__(self, raw_request):
        self.__dict__ = self.parse_headers(raw_request)

    def parse_headers(self, raw_request):
        headers = {}
        try:
            parse_method_resources_http_version(headers, raw_request)
        except ValueError as e:
            logging.debug(f"{e} -> {raw_request}")
            return

        for pair in raw_request[1:]:
            if pair == b"\n":
                continue
            header, value = pair.decode("utf8").split(": ")
            headers[header.strip().lower()] = value.strip()
        return headers
