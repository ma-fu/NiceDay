import sqlite3, pandas as pd
from tabulate import tabulate as tabu
from os.path import isfile, getsize

class Model:
	def __init__(self, name):
		self.name = name

	def isSQLite3(self):
		if not isfile(self.name):
			return False
		if getsize(self.name) < 100:
			return False
		with open(self.name,"rb") as fd:
			header = fd.read(100)[:16]
		b16 = b"SQLite format 3\x00"
		return header == b16

	def df_tbls(self):
		with sqlite3.connect(self.name) as db:
			tbls_query = "select name from sqlite_master where type='table'"
			tbls_df = pd.read_sql(tbls_query,db)
			self.tbls_df = tbls_df
		return tbls_df
	def df_from_tbl(self,tbl_name):
		with sqlite3.connect(self.name) as db:
			sel_all = "select * from %s" % (tbl_name)
		return pd.read_sql(sel_all,db)

	def req_tbl_id(self,idxs):
		order = None
		while order != "q": 
			order = input("Type table num:")
			if order in idxs:
				break
		return order

	def tbl_from_idx(self,order):
		order = int(order)
		return self.tbls_df.iloc[order][0]

	def disp_sql(self,df,idx=False):
		clms = df.columns.values
		disp = tabu(df,headers=clms,tablefmt="psql",showindex=idx)
		print(disp)
		
if __name__ == "__main__":
	db = input("sqlite file here:")
	
