import sqlite3, os
# prompt user which db
input_call = "!!! Call your db !!! \n:"
db_name = input(input_call)
print_connect = "Your db is %s\n"\
"...Connecting" %(db_name)
print_wrong_db = "Your db is not exists"\
"\nPlease place db same with sqlite.py"

cwd = os.listdir()
if db_name in cwd:
	print(print_connect)
else:
	print(print_wrong_db)
	exit()

# connect sqlite3 module



