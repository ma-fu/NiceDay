def isSQLite3(filename):
	from os.path import isfile, getsize
	if not isfile(filename):
		return False
	if getsize(filename) < 100:
		return False
	
	with open(filename,"rb") as fd:
		header = fd.read(100)[:16]
		b16 = b"SQLite format 3\x00"
	return header == b16

