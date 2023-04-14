ask_filename = "type filename you want to read"
filename = input(ask_filename)

with open(filename, "rb") as fd:
	header = fd.read(101) #100
#check SQLite or not
"""
var = b"SQLite format 3\x00"
b16 = header[:16]
x = var == b16
print(x)
"""
print(header)
print(len(header))

