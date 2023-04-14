import sqlite3, os


def isSQLite3(filename):
	isfile, getsize = os.path.isfile,\
os.path.getsize
	if not isfile(filename):
		return False
	if getsize(filename) < 100:
		return False
	with open(filename,"rb") as fd:
		header = fd.read(100)[:16]
		b16 = b"SQLite format 3\x00"
	return header == b16


# some string values here
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
con = sqlite3.connect(db_name)
cur = con.cursor()

	

