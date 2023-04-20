import sqlite3, os
from sql import Model

ask_file  = "db name:"

db_name = input(ask_file)

model = Model(db_name)

if model.isSQLite3():

	print("Successfuly connect %s!\n" % (db_name))

else:

	print("%s is not SQLite3" % (db_name))

	exit()

# Display tables 

df = model.get_tbls_df()

model.loop_main(df)






	

