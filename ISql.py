from os.path import isfile, getsize


def isSQLite3(filename):
# file exists or not
	if not isfile(filename):
		return False
# sqlite file is more than 100bytes
	if getsize(filename) < 100:
		return False
# read file as binary	
	with open(filename,"rb") as fd:

		header = fd.read(100)[:16]

		b16 = b"SQLite format 3\x00"
# return True or False
	return header == b16

# case using as lanch
if __name__ == "__main__":

	f_name = input("file you want check:")

	x = isSQLite3(f_name)

	print(x)
