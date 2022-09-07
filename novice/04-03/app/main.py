from flask import Flask
from flask import render_template
from flask import request
import psycopg2

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    conn = psycopg2.connect(
        host="localhost",
        database="ngaji",
        user="postgres",
        password="tiyanmoe")
    
    curs = conn.cursor()    
    if request.method == "POST":
        tanggal = request.form.get("tanggal")
        nama = request.form.get("nama")
        judul = request.form.get("judul")
        detail = request.form.get("detail")
        query = f"insert into ppqs(tanggal, nama, judul, detail) values('{tanggal}', '{nama}', '{judul}', '{detail}')"
        curs.execute(query)
        conn.commit()

    print(request.method)
    query = f"select * from ppqs"
    curs.execute(query)
    data = curs.fetchall()
    curs.close()
    conn.close()
    return render_template("index.html", context=data)

if __name__ == "__main__":
    app.run()