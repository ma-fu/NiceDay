import sqlite3, pandas as pd, re, time
from tabulate import tabulate as tabu
from os.path import isfile, getsize

class Model:
	def __init__(self, db):
		self.db = db

	def isSQLite3(self):
		if not isfile(self.db):
			return False
		if getsize(self.db) < 100:
			return False
		with open(self.db,"rb") as fd:
			header = fd.read(100)[:16]
		b16 = b"SQLite format 3\x00"
		return header == b16

	def tbls_df(self):
		q = "select name from sqlite_master where type='table'"
		with sqlite3.connect(self.db) as db:
			tbls_df = pd.read_sql(q,db)
			self.tbls_df = tbls_df
			return tbls_df

	def tbl_df(self,tbl_name):
		q = "select * from %s" % (tbl_name)
		with sqlite3.connect(self.db) as db:
			return pd.read_sql(q,db)

	def Inserter(self,data):
		clms,vls,tbl = data
		esc = re.sub("[\w|\d]*[^,]","?",data[clms])
		q = "insert into %s(%s) values (%s)" %  (data[tbl],data[clms],esc)
		with sqlite3.connect(self.db) as db:
			cur = db.cursor()
			cur.execute(q,data[vls])	
			db.commit()
		time.sleep(1)

	def tbl_name(self,idx):
		idx = int(idx)
		return self.tbls_df.iloc[idx][0]

	def clms_tbl_nam(self,tbl_nam):
		q = "pragma table_info(%s)" % tbl_nam
		with sqlite3.connect(self.db) as db:
			return pd.read_sql(q,db).name

	def disp_sql(self,df,idx=False):
		clms = df.columns.values
		disp = tabu(df,headers=clms,tablefmt="psql",showindex=idx)
		print(disp)

class Asker(Model):

	def ask_tbl_id(self,idxs):
		order = None
		while order != "q": 
			order = input("Type table num:")
			if order in idxs:
				break
		return order
	
	def ask_ins_data(self,df):
		clms_str = ""
		usr_vl = [] 
		for cl in df.columns:
			vl = "" 
			if df[cl].dtypes=="int64":
				print("\tNumber\ts:skip")
				while not vl.isnumeric():
					vl = input("%s:" % cl)
					if vl=="s":
						break
					if vl.isnumeric():
						clms_str += cl+","
						usr_vl.append(int(vl))
			else:
				vl = input("%s:" % cl)
				clms_str += cl+","
				usr_vl.append(vl)
		return {"clms":clms_str[:-1],"vls":usr_vl}

	def tbl_info(self,tbl_id):
		tbl_nam = super().tbl_name(tbl_id)
		tbl_df = super().tbl_df(tbl_nam)
		super().disp_sql(tbl_df)
		print("\tinsert:i")
		return tbl_nam, tbl_df

	def case_insert(self,tbl_df, tbl_nam):
		data = self.ask_ins_data(tbl_df)
		data["tbl"] = tbl_nam
		clms,vls,tbl = data 
		q = "insert into %s(%s) values (%s)" %  (data[tbl],data[clms],data[vls])
		return data
		
	def confirm_ins(self,data):
		yn = input("Would you like to save?(y/n)")
		if yn =="y":
			print("Saving")
			super().Inserter(data)
		else:
			print("Bye")
		
if __name__ == "__main__":
	pass
	
	
