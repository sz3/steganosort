import sys
from json import dumps

from flask import Flask
from steganosort.util import dict_encode


app = Flask(__name__, static_url_path='')


@app.route('/')
def index():
    res = {str(i): i for i in range(32)}
    res = dict_encode(res, b'helloworld')
    return dumps(res)


if __name__ == '__main__':
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 8000
    app.run(host='0.0.0.0', port=port)
