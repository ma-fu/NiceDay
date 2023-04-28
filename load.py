
def tbl_info(tbl_id):
	tbl_nam = asker.tbl_name(tbl_id)
	tbl_df = asker.tbl_df(tbl_nam)
	asker.disp_sql(tbl_df)
	print("\tinsert:i")
	return tbl_nam, tbl_df

def case_insert(tbl_df):
	data = asker.ask_ins_data(tbl_df)
	data["tbl"] = tbl_nam
	clms,vls,tbl = data 
	q = "insert into %s(%s) values (%s)" %  (data[tbl],data[clms],data[vls])
	return data
	
def confirm_ins(data):
	yn = input("Would you like to save?(y/n)")
	if yn =="y":
		print("Saving")
		asker.Inserter(data)
	else:
		print("Bye")

from sql import Asker
	
ask_file  = "db name:"
db_name = input(ask_file)

asker = Asker(db_name)

if asker.isSQLite3():
	print("Successfuly connect %s!" % (db_name))
else:
	print("%s is not SQLite3" % (db_name))
	exit()

tbls_df = asker.tbls_df()

# Display table data or some operations 
tbl_ids = list(map(str, tbls_df.index))
order = None
tbl_id = None
while order !="q":
	# First time or typed 't'
	if order is None or order=="t":
		asker.disp_sql(tbls_df,idx=True)

	# Insert mode	
	if order=="i":
		order = tbl_id
		data = case_insert(tbl_df)
		confirm_ins(data)

	# Usr value not in tble menu
	if order not in tbl_ids:
		tbl_id = asker.ask_tbl_id(tbl_ids) 
	else:
		tbl_id = order
	
	# Prompt which tbl
	if tbl_id != "q":
		tbl_nam,tbl_df = tbl_info(tbl_id)
		
	print("\ttbls:t\texit:q\ttbl_id:")
	order = input("Continue?")
	
