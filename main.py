from web.server import Server
from web.mywsgi import WebApplication
from project.urls import url_patterns


def main(url_patterns):
    app = WebApplication(urls=url_patterns)
    server = Server(app)
    server.run()


if __name__ == "__main__":
    main(url_patterns)
