import sqlite3, os

from ISql import isSQLite3

ask_file  = "db name:"

db_name = input(ask_file)

yes_file = "Successfuly connect %s!\n" % (db_name) 

no_file = "%s is not SQLite3" % (db_name)

if isSQLite3(db_name):

	print(yes_file)

else:

	print(no_file)

	exit()

# connect sqlite3 module

which_table = "Which table?\n"\
\


print(which_table)

"""
con = sqlite3.connect(db_name)

cur = con.cursor()
"""

	

