import sqlite3

conn = sqlite3.connect('drill2.db')

with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_files( \
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        col_finame TEXT \
        )")
    conn.commit()
conn.close()

conn = sqlite3.connect('drill2.db')

with conn:
    cur = conn.cursor()
    cur.execute("INSERT INTO tbl_files(col_finame) VALUES (?)", ('information.docx',))
    cur.execute("INSERT INTO tbl_files(col_finame) VALUES (?)", ('Hello.txt',))
    cur.execute("INSERT INTO tbl_files(col_finame) VALUES (?)", ('myImage.png',))
    cur.execute("INSERT INTO tbl_files(col_finame) VALUES (?)", ('myMovie.mpg',))
    cur.execute("INSERT INTO tbl_files(col_finame) VALUES (?)", ('World.txt',))
    cur.execute("INSERT INTO tbl_files(col_finame) VALUES (?)", ('data.pdf',))
    cur.execute("INSERT INTO tbl_files(col_finame) VALUES (?)", ('myPhoto.jpg',))
    conn.commit()
conn.close()

conn = sqlite3.connect('drill2.db')

with conn:
    cur = conn.cursor()
    cur.execute("SELECT col_finame FROM tbl_files WHERE col_finame LIKE '%.txt'")
    varFile = cur.fetchall()
    print(varFile)



