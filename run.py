from flask import Flask
app = Flask(__name__)

import time

@app.route('/')
def hello_world():
    return 'Hello world!'


t = time.localtime()
current_time = time.strftime("%H:%M:%S", t)
print(current_time)


app.run(host='0.0.0.0',
        port=8080,
        debug=True)
