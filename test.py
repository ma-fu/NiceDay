import pandas as pd
from tabulate import tabulate as tabl
from sqlite3 import connect

sel_tbl = "select name from sqlite_master where type='table';"

with connect("2023.db") as db:
	df = pd.read_sql(sel_tbl,db)

clms = df.columns.values
fmt = "psql"

res = tabl(df,headers=clms,tablefmt=fmt)
"""
if __name__ == "__main__":
	idxs = list(map(str,df.index))
	order = None
	key = None
	while order not in idxs:
		print(res)
		print("exit :q")
		order = input("How can I help you?:")
		while key != "test": 
			key = input("help me")
			if key =="q":
				break
		if order == "q":
			print("phew I get out loop")
	
"""

print(list(res.index))
