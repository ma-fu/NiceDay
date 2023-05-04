from Pyobs.sql import Asker
	
ask_file  = "Your Sqlite3 here:"
db_name = input(ask_file)

if db_name=="":
	db_name = "2023.db"

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
		data = asker.case_insert(tbl_df, tbl_nam)
		asker.confirm_ins(data)
	
	if order=="u":
		order = tbl_id
		asker.ask_up_data(tbl_df)
		pass
		#ask data

	# Usr value not in tble menu
	if order not in tbl_ids:
		tbl_id = asker.ask_tbl_id(tbl_ids) 
	else:
		tbl_id = order
	
	# Prompt which tbl
	if tbl_id != "q":
		tbl_nam,tbl_df = asker.tbl_info(tbl_id)
		
	print("\ttbls:t\texit:q\ttbl_id:")
	order = input("Continue?")

exit()
