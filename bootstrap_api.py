from argparse import ArgumentParser

HEADER_STRING = """import json
import os

from flask import Flask, request

DEFAULT_HOST = "{host}"
DEFAULT_PORT = {port}

app = Flask(__name__)
"""


ENDPOINT_STRING = """@app.route('/', methods=['GET'])
def index():
    print("REQUEST HEADERS")
    print(request.headers)
    return "ENDPOINT: index"
"""

SCRIPT_STRING = """if __name__ == "__main__":

    host = os.getenv("FLASK_HOST", DEFAULT_HOST)
    port = os.getenv("FLASK_PORT", DEFAULT_PORT)
    debug = os.getenv("FLASK_DEBUG", True)

    app.run(host=host, port=port, debug=debug)
"""


def construct_endpoint(path='', fn_name='f'):
    return """@app.route('/{0}', methods=['GET', 'POST'])
def {1}():
    print("REQUEST HEADERS")
    print(request.headers)
    return "ENDPOINT: {2}"
""".format(path, fn_name, fn_name)


if __name__ == "__main__":

    parser = ArgumentParser()
    parser.add_argument('-p', metavar='text', nargs='?', default='app.py', help="file path")
    parser.add_argument('-endpoints', metavar='text', nargs='?', default=None)
    parser.add_argument('-host', metavar='text', nargs='?', default=None)
    parser.add_argument('-port', metavar='text', nargs='?', default=None)

    args = parser.parse_args()

    host = args.host or "localhost"
    port = args.port or 8888
    HEADER_STRING = HEADER_STRING.format(host=host, port=port)

    # Construct endpoint section
    endpoints = []
    if args.endpoints:
        endpoints = list(set([e.strip() for e in args.endpoints.split(',')]))
        ENDPOINT_STRING += ''.join([construct_endpoint(name) for name in endpoints])

    content = "\n\n".join([HEADER_STRING, ENDPOINT_STRING, SCRIPT_STRING])

    with open(args.p, 'w') as f:
        f.write(content)

    print("Successfully generated API: {}".format(args.p))
