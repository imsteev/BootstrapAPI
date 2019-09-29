# bootstrap-flask-api


## Prerequisites

## Usage
```
python3 ./bootstrap_api.py -endpoints "endpoint1, endpoint2, endpoint3" -host localhost -port 8080
```

## Defaults
- host = "localhost"
- port = 8888

Note: all APIs will be generated with an `index` endpoint that can be reached at the root path aka `<host>:<port>`

### Example
```
Stephens-MacBook-Pro:bootstrap_flask_api stephenchung$ python ./bootstrap_api.py -endpoints "add, subtract, divide, multiply" -host 127.0.0.1
Successfully generated API: app.py
Stephens-MacBook-Pro:bootstrap_flask_api stephenchung$ cat app.py
import json
import os

from flask import Flask, request

DEFAULT_HOST = "127.0.0.1"
DEFAULT_PORT = 8888

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    print("REQUEST HEADERS")
    print(request.headers)
    return "ENDPOINT: index"
@app.route('/divide', methods=['GET', 'POST'])
def f():
    print("REQUEST HEADERS")
    print(request.headers)
    return "ENDPOINT: f"
@app.route('/subtract', methods=['GET', 'POST'])
def f():
    print("REQUEST HEADERS")
    print(request.headers)
    return "ENDPOINT: f"
@app.route('/multiply', methods=['GET', 'POST'])
def f():
    print("REQUEST HEADERS")
    print(request.headers)
    return "ENDPOINT: f"
@app.route('/add', methods=['GET', 'POST'])
def f():
    print("REQUEST HEADERS")
    print(request.headers)
    return "ENDPOINT: f"


if __name__ == "__main__":

    host = os.getenv("FLASK_HOST", DEFAULT_HOST)
    port = os.getenv("FLASK_PORT", DEFAULT_PORT)
    debug = os.getenv("FLASK_DEBUG", True)

    app.run(host=host, port=port, debug=debug)
```

## Upcoming work
- Add option to supply config from file
- Dockerize
