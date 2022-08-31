try:
    import psycopg2
    conn = psycopg2.connect(
        host="localhost",
        database="exqs",
        user="postgres",
        password="tiyanmoe")

    curs = conn.cursor()

    nama = "anggita"
    umur = "24"
    query = f"insert into siswa(nama, umur) values('{nama}', {umur})"
    curs.execute(query)
    conn.commit()
    print("data sudah masuk gais")

except Exception as e:
    print(e)