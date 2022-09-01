# memasukkan package flask
from flask import Flask
app = Flask(__name__)

# membuat halaman di web
@app.route('/')
def index():
    return 'Index Page'

@app.route('/hello')
def hello():
    return 'Hello, World'

# sintak output link
if __name__ == "__main__":
    app.run()