import os
from flask import Flask

app = Flask(__name__)

@app.route('/<path:path>')
@app.route('/')
def begin(path = '/'):
    tempReturn = ''
    return tempReturn

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host = '0.0.0.0', port = port, debug = True)
