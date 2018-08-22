import os
from web.mywsgi import BASE_DIR, PROJECT_NAME


def render(request, template_path, template_args):
    directory = os.path.join(BASE_DIR, os.path.join(PROJECT_NAME, template_path))
    with open(f"{directory}", 'r') as template:
        content = template.read()
        for parameter, arg in template_args.items():
            content = content.replace("{ %s }" % parameter, arg)
        return content.encode("utf8")


def parse_method_resources_http_version(d, raw_request):
    first_line = raw_request[0].decode("utf8").split(" ")
    if len(first_line) == 3:
        d['method'], d['resource'], d['version'] = first_line
    elif len(first_line) == 2:
        d['method'], d['version'] = first_line
