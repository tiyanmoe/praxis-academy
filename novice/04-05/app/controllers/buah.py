import psycopg2
from flask import Flask
from flask import render_template
from flask import request
app = Flask(__name__)

def index():
    conn = psycopg2.connect(
        host="localhost",
        database="exqs",
        user="postgres",
        password="tiyanmoe")
    
    curs = conn.cursor()    
    if request.method == "POST":
        nama = request.form["nama"]
        detail = request.form["detail"]
        query = f"insert into buah(nama, detail) values('{nama}', '{detail}')"
        curs.execute(query)   # untuk mengeksekusi query
        conn.commit()

    print(request.method)
    query = f"select * from buah"
    curs.execute(query)
    data = curs.fetchall()
    return render_template("index.html", context=data)