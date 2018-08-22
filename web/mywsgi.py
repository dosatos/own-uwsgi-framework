import os


BASE_DIR = os.getcwd()
PROJECT_NAME = 'project'


class URLMixin:
    def __init__(self, urls):
        self.urls = {}
        self.register_urls(urls)

    def register_urls(self, urls):
        self.urls = {}
        for url, vu in urls:
            self.urls[url] = vu

    def route(self, request):
        view = self.match_view(request)
        return view(request)

    def match_view(self, request):
        try:
            url = parse_url(request)
            return self.urls[url]
        except KeyError:
            return self.url_mismatch_view


class ViewMixin:
    def url_mismatch_view(self, request):
        url = parse_url(request)
        return f"Wrong url: {url}".encode('utf8')


class WebApplication(ViewMixin, URLMixin):
    def __init__(self, urls):
        super().__init__(urls=urls)

    def __call__(self, request, start_response):
        start_response("HTTP/1.1 200 OK", [('Content-Type', 'text/html')])
        html = self.route(request)
        return html


def parse_url(request):
    return request.resource.split("&")[0]