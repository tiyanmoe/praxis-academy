from flask import Flask
app = Flask(__name__)

@app.route("/")
def index(): 
    return 'Halaman Index'

@app.route('/heh')
def heh(): 
    return "Hello cur"

# membuat kondisional
if __name__ == "__main__":
    app.run()