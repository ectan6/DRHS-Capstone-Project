# connecting to a database - new one named elements.db
connection = sqlite3.connect('element.db')

# creating a cursor
c = connection.cursor()

# create a table
c.execute("""CREATE TABLE elements (
	element_ID text, 
	level integer)
""")

# datatypes: NULL, INTEGER, REAL, TEXT, BLOB

# commit command
connection.commit()

# close the connection
connection.close()
