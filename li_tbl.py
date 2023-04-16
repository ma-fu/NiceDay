import sqlite3
import pandas as pd
from tabulate import tabulate

ask_file = "Database file:"

db_file = input(ask_file)

#con = sqlite3.connect(db_file)

#con.text_factory = str

que = "select name from sqlite_master"\
" where type = 'table';"

#cur = con.cursor()

#result = cur.execute(que).fetchall()

"""
(1),(2),(3) >> (1, 2, 3)
zip(*result)


list(zip(*result))[0]

[(1),(2),(3)] >> [(1,2,3)]
"""

#df = pd.DataFrame(result,columns=["test"])

with sqlite3.connect(db_file) as con:
	df = pd.read_sql(que,con)


columns = df.columns.values

fmt = "psql"

fm_sql = tabulate(df,headers=columns,tablefmt=fmt)

print(fm_sql)
