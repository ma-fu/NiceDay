from sql import Model

ask_file  = "db name:"
db_name = input(ask_file)

model = Model(db_name)

if model.isSQLite3():
	print("Successfuly connect %s!" % (db_name))
else:
	print("%s is not SQLite3" % (db_name))
	exit()

tbls_df = model.df_tbls()

# Display table data 
tbls_idx = list(map(str, tbls_df.index))
order = None
while order !="q":
	if order is None or order=="t":
		model.disp_sql(tbls_df,idx=True)
	print("\texit:q")

	if order not in tbls_idx:
		tbl_idx = model.req_tbl_id(tbls_idx) 
	else:
		tbl_idx = order

	if tbl_idx != "q":
		tbl_name = model.tbl_from_idx(tbl_idx)
		tbl_df = model.df_from_tbl(tbl_name)
		model.disp_sql(tbl_df)
		
	print("\ttbls:t\texit:q\ttbls_id:")
	order = input("Continue?")









	

