from flask import Flask
app = Flask(__name__)

@app.route("/")
def hadolek(): # membuat fungsi
    return "halodoc halodek"

# membuat kondisional
if __name__ == "__main__":
    app.run()