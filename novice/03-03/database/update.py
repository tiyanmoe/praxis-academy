try:
    import psycopg2
    conn = psycopg2.connect(
        host="localhost",
        database="exqs",
        user="postgres",
        password="tiyanmoe")

    curs = conn.cursor()

    namaLama = "anggita"

    namaBaru = "mayastika"
    umurBaru = 25
    query = f"update siswa set nama='{namaBaru}', umur={umurBaru} where nama='{namaLama}'"

    curs.execute(query)
    conn.commit()
    print("data sudah terupdate yaaa")

except Exception as e:
    print(e)