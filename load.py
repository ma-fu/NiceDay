import sqlite3, os
from sql import Model

ask_file  = "db name:"

db_name = input(ask_file)

model = Model(db_name)

if model.isSQLite3():

	print("Successfuly connect %s!" % (db_name))

else:

	print("%s is not SQLite3" % (db_name))

	exit()

# Display tables 

tbls_df = model.df_tbls()

# convert integer to string in list

tbls_idx = list(map(str, tbls_df.index))

order = None

while order !="q":
	model.disp_sql(tbls_df)
	print("\texit:q")
# Display table data 
# get id user would like
	idx = model.req_tbls_id(tbls_idx)
	tbl_name = model.tbl_from_idx(idx)
	tbl_df = model.df_from_tbl(tbl_name)
	model.disp_sql(tbl_df)
	order = input("Continue?")









	

