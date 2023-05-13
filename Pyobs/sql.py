import sqlite3, pandas as pd, re, time
from tabulate import tabulate as tabu
from os.path import isfile, getsize

class Source:
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

	def Executer(self,q,v=False):
		with sqlite3.connect(self.db) as db:
			cur = db.cursor()
			if v:
				cur.execute(q,v)
			else:
				cur.execute(q)
			db.commit()
		time.sleep(1)
	
	def df_maker(self,q):
		with sqlite3.connect(self.db) as db:
			df = pd.read_sql(q,db)
		return df

	def tbls_df(self):
		q = "select name from sqlite_master where type='table'"
		tbls_df = self.df_maker(q)
		self.tbls_df = tbls_df
		return tbls_df

	def tbl_df(self,tbl_name):
		q = "select * from %s" % (tbl_name)
		return self.df_maker(q)

	def q_plus_minus(self,data):
		q = "update %(tbl)s set %(cl)s = %(cl)s"\
		"%(vl)s where id in (%(whe)s)" % data
		return q

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
	
	def dic_id_cls(self,df):
		return {str(i):c for i,c in enumerate(df.columns)}

	def is_in_dic(self,key,dic):
		if key in dic:
			return dic[key]
		else:
			print("value not in list")
			return False
			
		return dic[key] if key in dic else False

	def is_cl_int(self,df,cl):
		if df[cl].dtypes=="int64":
			return True
		else:
			return False

	def merge_data(self,df,cls,vls):
		data = list(map(lambda cl,vl:int(vl) if self.is_cl_int(df,cl) else vl,cls,vls))
		cls = ",".join(cls)
		data = {"cls":cls,"vls":data}
		return data
	
	def plc_hldr(self,data):
		ph = ",".join(list(map(lambda x: "?",data)))
		return ph

	def q_insert(self,data):
		q = "insert into %(tbl)s(%(cls)s) values (%(ph)s)" % data
		return q

	def q_plus(self,data):
		q = "update %(t)s set %(c)s where id in (%(w)s)" % data
		return q

	def q_new_tbl(self,data):
####
		q = "create table %(t)s"

	def plus_minus_cls(self,cls,p="+"):
		x = ",".join(list(map(lambda d: "%(d)s=%(d)s%(p)s?" % {"d":d,"p":p},cls)))
		return x


class Asker(Source):

	def ask_num_loop(self,ask):
		num = ""
		while not num.isnumeric():
			num = input(ask)
		return num

	def ask_tbl_id(self,idxs):
		idx = None
		while idx != "q": 
			idx = input("Type table num:")
			if idx in idxs:
				break
		return idx
	
	def ask_which_cls(self,df):
		id_cls = super().dic_id_cls(df)
		print("\t"+"\t".join(["%s:%s" % (k,v) for k,v in id_cls.items()]))
		usr = input("\t\t\tColumn id:")
		usr = usr.split(",")
		cls = [id_cls[n] for n in usr if n in id_cls]
		return cls

	def ask_where_id(self):
		return input("\t\t\tWhere id:")

	def ask_vls(self):
		vls = input("\t\t\tValues:")
		return vls.split(",")

	def ask_int_cl(self,df):
		idx_cls = super().dic_id_cls(df)
		data = {}
		ask = "Which column?\n\t%s:" % idx_cls
		cl_id = self.ask_num_loop(ask)
		cl = super().is_in_dic(cl_id,idx_cls)
		if cl:
			if super().is_cl_int(df,cl):
				return cl
			else:
				return False
		else:
			return False

	def tbl_info(self,tbl_id):
		tbl_nam = super().tbl_name(tbl_id)
		tbl_df = super().tbl_df(tbl_nam)
		super().disp_sql(tbl_df)
		print("\tinsert:i\t+:p\t-:m")
		return tbl_nam, tbl_df

	def ask_new_tbl(self):
		data = {}
		tbl = input("type new tbl name:")
		idx = input("You need idx?:")
		if idx:
			data["Id"] = "Id integer primary key autoincrement,"
		else:
			data["Id"] = False

	def case_new_tbl(self):
		pass


	def case_insert(self,df,tbl):
		cls = self.ask_which_cls(df)
		vls = self.ask_vls()
		data = self.merge_data(df,cls,vls)
		ph = self.plc_hldr(cls)
		data["tbl"] = tbl
		data["ph"] = ph
		q = self.q_insert(data)
		return q,data["vls"]

	def case_plus_minus(self,df,tbl,p="+"):
		cls = self.plus_minus_cls(self.ask_which_cls(df),p)
		vls = self.ask_vls()
		wid = self.ask_where_id()
		data = {"t":tbl,"c":cls,"w":wid}
		q = self.q_plus(data)
		return q,vls

	def confirm_exe(self,q,vls):
		yn = input("Would you like to save?(y/n)")
		if yn =="y":
			print("Saving")
			super().Executer(q,vls)
		else:
			print("Bye")

		
if __name__ == "__main__":
	asker = Asker("2023.db")
	tbl = "Refrigerator"
	df = asker.tbl_df(tbl)

	cls = asker.plus_minus_cls(asker.ask_which_cls(df))
	vls = asker.ask_vls()
	wid = asker.ask_where_id()
	data = {"t":tbl,"c":cls,"v":vls,"w":wid}
	q = asker.q_plus(data)
	
	print(q)




