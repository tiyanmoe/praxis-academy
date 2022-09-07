from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
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
    query = f"select * from ppqs order by tanggal asc"
    curs.execute(query)
    data = curs.fetchall()
    curs.close()
    conn.close()
    return render_template("index.html", context=data)

@app.route("/detail/<ppqs_id>")
def detail(ppqs_id):
    conn = psycopg2.connect(
        host="localhost",
        database="ngaji",
        user="postgres",
        password="tiyanmoe")
    
    curs = conn.cursor()
    query = f"select * from ppqs where id = {ppqs_id}"
    curs.execute(query)
    data = curs.fetchone()
    curs.close()
    conn.close()
    print(data)
    return render_template("detail.html", context=data)

@app.route("/delete/<ppqs_id>")
def delete(ppqs_id):
    conn = psycopg2.connect(
        host="localhost",
        database="ngaji",
        user="postgres",
        password="tiyanmoe")
    
    curs = conn.cursor()
    query = f"delete from ppqs where id = {ppqs_id}"
    curs.execute(query)
    conn.commit()
    curs.close()
    conn.close()
    return redirect("/")

@app.route("/update/<ppqs_id>", methods=["GET", "POST"])
def update(ppqs_id):
    conn = psycopg2.connect(
        host="localhost",
        database="ngaji",
        user="postgres",
        password="tiyanmoe")
    
    curs = conn.cursor()
    if request.method == "POST":
        tanggal = request.form["tanggal"]
        nama = request.form["nama"]
        judul = request.form["judul"]
        detail = request.form["detail"]
        query = f"update ppqs set tanggal = '{tanggal}', nama = '{nama}', judul = '{judul}', detail = '{detail}' where id = {ppqs_id}"
        curs.execute(query)
        conn.commit()
        return redirect("/")
    
    query = f"select * from ppqs where id = {ppqs_id}"
    curs.execute(query)
    data = curs.fetchone()
    curs.close()
    conn.close()
    return render_template("update.html", context=data)

if __name__ == "__main__":
    app.run()