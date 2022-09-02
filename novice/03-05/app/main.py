from flask import Flask
from flask import render_template
from flask import request
import psycopg2

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
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
        # print(request.method)
        # print(20*"=")
        # print(request.form)
        # print(request.form["nama"])
        # print(request.form["detail"])
        # print(20*"=")
        query = f"insert into buah(nama, detail) values('{nama}', '{detail}')"
        curs.execute(query)   # untuk mengeksekusi query
        conn.commit()
        curs.close()
        conn.close()

    print(request.method)
    query = f"select * from buah"
    curs.execute(query)
    data = curs.fetchall()

    # data = ["apel", "anggur", "amer"] ==> dummy (data percobaan) bisa dimatikan fungsinya
    return render_template("index.html", context=data)

if __name__ == "__main__":
    app.run()