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
tbl_ids = list(map(str, tbls_df.index))
order = None
tbl_id = None
while order !="q":
	if order is None or order=="t":
		model.disp_sql(tbls_df,idx=True)
	
	if order=="i":
		order = tbl_id
		data = model.req_ins_data(tbl_df)
		data["tbl"] = tbl_nam
		clms,esc,vls,tbl = data 
		q = "insert into %s(%s) values (%s)" %  (data[tbl],data[clms],data[esc])
		print(q)
		print(data[vls])
		yn = input("Would you like to save?(y/n)")
		if yn =="y":
			print("saving")
			model.insert_data(data)
		else:
			print("bye")

	if order not in tbl_ids:
		tbl_id = model.req_tbl_id(tbl_ids) 
	else:
		tbl_id = order

	if tbl_id != "q":
		tbl_nam = model.tbl_from_id(tbl_id)
		tbl_df = model.df_from_tbl(tbl_nam)
		model.disp_sql(tbl_df)
		print("\tinsert:i")
		
	print("\ttbls:t\texit:q\ttbl_id:")
	order = input("Continue?")
	









	

