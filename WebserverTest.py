import numpy
from flask import Flask, send_from_directory
app = Flask(__name__,static_url_path="/WS_UI")

@app.route('/')
def index():
    return send_from_directory("WS_UI","index.html")
 

if __name__ == '__main__':
    app.run(debug=True)