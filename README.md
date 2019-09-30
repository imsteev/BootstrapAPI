# bootstrap-flask-api


### Prerequisites
- Python3
- Flask

### Usage
```
usage: bootstrap_api.py [-h] [-n NAME] [-e ENDPOINTS] [-host HOST]
                        [-port PORT]

optional arguments:
  -h, --help            show this help message and exit
  -n NAME, --name NAME  File name to be generated in current directory.
                        Default: app.py
  -e ENDPOINTS, --endpoints ENDPOINTS
                        Comma separated string of endpoints
  -host HOST            Host address to be reached at. Default: "localhost"
  -port PORT            Port to listen at. Default port: 8888
```

### Defaults
- host = "localhost"
- port = 8888

Note: all APIs will be generated with an `index` endpoint that can be reached at the root path aka `<host>:<port>`

### Example
```
Stephens-MacBook-Pro:bootstrap_flask_api stephenchung$ python ./bootstrap_api.py -e "add, subtract, divide, multiply" -host 127.0.0.1
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
    return "ENDPOINT: /"


@app.route('/subtract', methods=['GET', 'POST'])
def subtract():
    return "ENDPOINT: /subtract"


@app.route('/add', methods=['GET', 'POST'])
def add():
    return "ENDPOINT: /add"


@app.route('/multiply', methods=['GET', 'POST'])
def multiply():
    return "ENDPOINT: /multiply"


@app.route('/divide', methods=['GET', 'POST'])
def divide():
    return "ENDPOINT: /divide"


if __name__ == "__main__":

    host = os.getenv("FLASK_HOST", DEFAULT_HOST)
    port = os.getenv("FLASK_PORT", DEFAULT_PORT)
    debug = os.getenv("FLASK_DEBUG", True)

    app.run(host=host, port=port, debug=debug)
```

### Upcoming work
- Add option to supply config from file
- Dockerize
