from Pyobs.sql import Asker
	
ASK_FILE  = "Your Sqlite3 here:"
DEFAULT = "2023.db"
DB_PATH = input(ASK_FILE)

if DB_PATH=="":
	DB_PATH = DEFAULT

asker = Asker(DB_PATH)

if asker.isSQLite3():
	print(f"Successfuly connect {DB_PATH}!")
else:
	print(f"{DB_PATH} is not SQLite3")
	exit()

TABLES_DF = asker.tbls_df()

# Display table data or some operations 
TABLE_IDS = list(map(str, TABLES_DF.index))
ORDER = None
TABLE_ID = None
while ORDER !="q":
	# First time or typed 't'
	if ORDER is None or ORDER=="t":
		asker.disp_sql(TABLES_DF,idx=True)

	# Insert mode	
	if ORDER=="i":
		ORDER = TABLE_ID
		QUERY,VALUES = asker.case_insert(TABLE_DF, TABLE_NAME)
		asker.confirm_exe(QUERY,VALUES)
	
	if ORDER=="p":
		ORDER = TABLE_ID
		QUERY,VALUE = asker.case_plus_minus(TABLE_DF,TABLE_NAME)
		asker.confirm_exe(QUERY,VALUE)
		#ask data

	if ORDER=="m":
		ORDER=TABLE_ID
		QUERY,VALUE = asker.case_plus_minus(TABLE_DF,TABLE_NAME,"-")
		asker.confirm_exe(QUERY,VALUE)

	if ORDER=="n":
		QUERY = asker.case_new_tbl()
		asker.confirm_exe(QUERY)

	# Usr value not in tble menu
	if ORDER not in TABLE_IDS:
		TABLE_ID = asker.ask_tbl_id(TABLE_IDS) 
	else:
		TABLE_ID = ORDER
	
	# Prompt which tbl
	if TABLE_ID != "q":
		TABLE_NAME,TABLE_DF = asker.tbl_info(TABLE_ID)
		
	print("\ttbls:t\texit:q\tTABLE_ID:")
	print("\tnew:n")
	ORDER = input("Continue?")

exit()
