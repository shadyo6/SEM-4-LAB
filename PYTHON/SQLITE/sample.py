import sqlite3, sys
from contextlib import closing

def dbConnection(file):
	try:
		conn=sqlite3.connect(file)
		return conn
	except:
		print("Database Connection failed")
		sys.exit()

def exQuery(query,c):
	try:
		c.execute(query)
	except:
		print("Query Execution error")


def selectFromall(conn,c):
	query = ("select * from sample")
	exQuery(query, c)
	print("Result:", c.fetchall())

def createTable(conn,c):
	query = ("CREATE TABLE if not exists sample(id integer, name text, Primary key(id))")
	exQuery(query, c)
	conn.commit()

def main():
	conn = dbConnection("C:\\Users\\admin\\Documents\\Sqlite experiments\\01sample.sqlite")
	with closing(conn.cursor()) as c:

		createTable(conn,c)
		selectFromall(conn,c)

if __name__=='__main__':
	main()