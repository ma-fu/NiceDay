import sqlite3, os

import pandas as pd

from ISql import isSQLite3

from tabulate import tabulate


ask_file  = "db name:"

db_name = input(ask_file)

yes_file = "Successfuly connect %s!\n" % (db_name) 

no_file = "%s is not SQLite3" % (db_name)

if isSQLite3(db_name):

	print(yes_file)

else:

	print(no_file)

	exit()


# Display tables 

which_table = "Which table?:"

que = "select name from sqlite_master"\
\
" where type = 'table';"

with sqlite3.connect(db_name) as con:

	df = pd.read_sql(que,con)

columns = df.columns.values

fmt = "psql"

fm_sql = tabulate(df,headers=columns,tablefmt=fmt)

print(fm_sql)


# Select table

ask_table = input(which_table)

print(ask_table)

# Test


	

