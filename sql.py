import sqlite3, pandas as pd
from tabulate import tabulate as tabu
from os.path import isfile, getsize


class Model:

	def __init__(self, name):
		self.name = name

	def get_tbls_df(self):
		with sqlite3.connect(self.name) as db:
			tbls_query = "select name from sqlite_master where type='table'"
			tbls_df = pd.read_sql(tbls_query,db)
			self.tbls_df = tbls_df
		return tbls_df

	def get_tbl_df(self,tbl_name):
		with sqlite3.connect(self.name) as db:
			sel_all = "select * from %s" % (tbl_name)
		return pd.read_sql(sel_all,db)

	def sqlike_df(self,df):
		clms = df.columns.values
		return tabu(df,headers=clms,tablefmt="psql")


	def isSQLite3(self):

		if not isfile(self.name):
			return False

		if getsize(self.name) < 100:
			return False

		with open(self.name,"rb") as fd:
			header = fd.read(100)[:16]

		b16 = b"SQLite format 3\x00"
		return header == b16

	def loop_main(self,df):
		order = None
		tbls_idx = list(map(str,df.index))

		while order not in tbls_idx: 
			print(self.sqlike_df(df))
			order = input("Type table num:")
			if order in tbls_idx:
				tbl_name = self.tbl_from_tbls(order)[0]
				tbl_df = self.get_tbl_df(tbl_name)
				print(self.sqlike_df(tbl_df))
				order = None
				input("type something")
			if order == "q":
				break
		return order

	def loop_tbl(self,df):
		pass
	
	def tbl_from_tbls(self,num):
		num = int(num)
		return self.tbls_df.iloc[num]
		
		
if __name__ == "__main__":
	db = input("sqlite file here:")
	
