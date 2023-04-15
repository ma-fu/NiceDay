import sqlite3

ask_file = "Database file:"

db_file = input(ask_file)

con = sqlite3.connect(db_file)

con.text_factory = str

que = "select name from sqlite_master"\
" where type = 'table';"

cur = con.cursor()

result = cur.execute(que).fetchall()

tbl_names = sorted(zip(*result[0]))

print(tbl_names)
