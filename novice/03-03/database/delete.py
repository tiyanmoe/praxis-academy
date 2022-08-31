try:
    import psycopg2
    conn = psycopg2.connect(
        host="localhost",
        database="exqs",
        user="postgres",
        password="tiyanmoe")

    curs = conn.cursor()

    nama = "mayastika"
    query = f"delete from siswa where nama='{nama}'"
    curs.execute(query)
    conn.commit()
    print("data berhasil dihapus!")

except Exception as e:
    print(e)