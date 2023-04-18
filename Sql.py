import sqlite3
from tabulate import tabulate as tabu
import pandas as pd

tbls = "select name from sqlite_master where type = 'table'"

class Model:

	def __init__(self, name):
		self.name = name

	def Tbls(self):
		with sqlite3.connect(self.name) as db:
			df = pd.read_sql(tbls,db)

		clms = df.columns.values
		return tabu(df,headers=clms,tablefmt="psql")

if __name__ == "__main__":
	x = Model("2023.db")
	y = Model.Tbls()
	print(y)
	
