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

	def Executer(self,q):
		with sqlite3.connect(self.db) as db:
			cur = db.cursor()
			cur.execute(q)
			db.commit()
	
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

	def Inserter(self,data):
		data["esc"] = re.sub("[\w|\d]*[^,]","?",data["clms"])
		q = "insert into %(tbl)s(%(clms)s) values (%(esc)s)" %  (data)
		with sqlite3.connect(self.db) as db:
			cur = db.cursor()
			cur.execute(q,data["vls"])	
			db.commit()
		time.sleep(1)
	
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
	
	def ask_which_cls(self,df):
		id_cls = super().dic_id_cls(df)
		print("\t".join(["%s:%s" % (k,v) for k,v in id_cls.items()]))
		usr = input("specify id 1 or 1,2,3:")
		usr = usr.split(",")
		cls = [id_cls[n] for n in usr if n in id_cls]
		return cls

	def ask_vls(self):
		vls = input("ex 1a or 1,a,3:")
		return vls.split(",")

	def merge_clvl(self,df,cls,vls):
		data = dict(map(lambda cl,vl:(cl,int(vl)) if self.is_cl_int(df,cl) else (cl,vl),cls,vls))
		return data
	
	def plc_hldr(self,data):
		ph = list(map(lambda x: "?",data))
		return ph

	def ask_int_cl(self,df):
		idx_cls = super().dic_id_cls(df)
		data = {}
		ask = "Which column?\n%s:" % idx_cls
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
		print("\tinsert:i\tplus:p")
		return tbl_nam, tbl_df

	def case_insert(self,tbl_df, tbl_nam):
		data = self.ask_ins_data(tbl_df)
		data["tbl"] = tbl_nam
		clms,vls,tbl = data 
		q = "insert into %s(%s) values (%s)" % (data[tbl],data[clms],data[vls])
		return data
		
	def confirm_ins(self,data):
		yn = input("Would you like to save?(y/n)")
		if yn =="y":
			print("Saving")
			super().Inserter(data)
		else:
			print("Bye")

		
if __name__ == "__main__":
	asker = Asker("2023.db")
	df = asker.tbl_df("Refrigerator")
	cls = asker.ask_which_cls(df)
	vls = asker.ask_vls()
	data = asker.merge_clvl(df,cls,vls)
	ph = asker.plc_hldr(data)
	ph = ",".join(ph)
	print(ph)



