from argparse import ArgumentParser

HEADER_STRING = """import json
import os

from flask import Flask, request

DEFAULT_HOST = "{host}"
DEFAULT_PORT = {port}

app = Flask(__name__)
"""


def construct_endpoint(path='', fn_name='f', methods=None):
    methods = methods or ['GET', 'POST']
    return """@app.route('/{0}', methods={1})
def {2}():
    return "ENDPOINT: {3}"
""".format(path, str(methods), fn_name, '/' + path)


ENDPOINT_STRING = construct_endpoint(path="", fn_name="index", methods=['GET'])

SCRIPT_STRING = """if __name__ == "__main__":

    host = os.getenv("FLASK_HOST", DEFAULT_HOST)
    port = os.getenv("FLASK_PORT", DEFAULT_PORT)
    debug = os.getenv("FLASK_DEBUG", True)

    app.run(host=host, port=port, debug=debug)
"""


if __name__ == "__main__":

    parser = ArgumentParser()
    parser.add_argument('-n', '--name', type=str, default='app.py', help="File name to be generated in current directory. Default: app.py")
    parser.add_argument('-e', '--endpoints', type=str, default=None, help="Comma separated string of endpoints")
    parser.add_argument('-host', type=str, default="localhost", help="Host address to be reached at. Default: \"localhost\"")
    parser.add_argument('-port', type=int, default=8888, help="Port to listen at. Default port: 8888")

    args = parser.parse_args()

    HEADER_STRING = HEADER_STRING.format(host=args.host, port=args.port)

    # Construct endpoint section
    endpoints = []
    if args.endpoints:
        endpoints = list(set([e.strip() for e in args.endpoints.split(',')]))  # remove dupes
        ENDPOINT_STRING += "\n\n"  # spacing after index
        ENDPOINT_STRING += '\n\n'.join([construct_endpoint(path=name, fn_name=name) for name in endpoints])

    content = "\n\n".join([HEADER_STRING, ENDPOINT_STRING, SCRIPT_STRING])

    with open(args.name, 'w') as f:
        f.write(content)

    print("Successfully generated API: {}".format(args.name))
