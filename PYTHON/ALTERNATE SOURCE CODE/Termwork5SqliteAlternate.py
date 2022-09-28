import sqlite3
from sqlite3 import Error

def dbConnect(file):
    conn = None
    try:
        conn = sqlite3.connect(file)
        print(conn,"\tVersion",sqlite3.version)
        return conn
    except Error as e:
        print(e)
        exit()
        
def createTable(conn):
    query = ("CREATE TABLE IF NOT EXISTS PRODUCTS(id integer, name text, qty integer, price real, primary key(id))")
    
    try:
        c = conn.cursor()
        c.execute(query)
        conn.commit()
        print("If table not exist then create")
    except:
        print("Failed to create table")
        
        
def insert(conn):
    try:
        n = int(input("Enter the number of records to be inserted: "))
        while n != 0:
            n = n-1
            id,name,qty,price = input("Enter prodId, name, quantity and price: ").split()
            query = "INSERT INTO PRODUCTS VALUES(?,?,?,?)"
            c = conn.cursor()
            c.execute(query,(id,name,qty,price))
            conn.commit()
    except Error as e:
        print(e)
    except ValueError as e:
        print(e)

def display(conn):
    query = "SELECT * FROM PRODUCTS"
    try:
        c = conn.cursor()
        c.execute(query)
        result = c.fetchall()
        print("Products: ")
        for line in result:
            print(line[0], line[1], line[2], line[3])
    except Error as e:
        print(e)

def update(conn):
    query = "UPDATE PRODUCTS SET PRICE = PRICE+(PRICE*0.1) WHERE PRICE < 50"
    try:
        c = conn.cursor()
        c.execute(query)
        conn.commit()
    except Error as e:
        print(e)

def delete(conn):
    query = "DELETE FROM PRODUCTS WHERE ID = ?"
    try:
        id = input("Enter the id to delete: ")
        c = conn.cursor()
        c.execute(query,(id))
        conn.commit()
    except Error as e:
        print(e)
    except ValueError as e:
        print(e)
        
def dispLessFourty(conn):
    query = "SELECT * FROM PRODUCTS WHERE QTY < 40"
    try:
        c = conn.cursor()
        c.execute(query)
        result = c.fetchall()
        for line in result:
            print(line[0], line[1], line[2], line[3])
    except Error as e:
        print(e)

def main():
    conn = dbConnect("products.db")
    while True:
        ch = (input("\n1.CREATE TABLE\t2.INSERT\t3.DISPLAY\t4.DELETE\t5.UPDATE\t6.DISPLAY < 40\t7.EXIT: "))
        if ch == '1':
            createTable(conn)
        elif ch == '2':
            insert(conn)
        elif ch == '3':
            display(conn)
        elif ch == '4':
            delete(conn)
        elif ch =='5':
            update(conn)
        elif ch == '6':
            dispLessFourty(conn)
        elif ch == '7':
            exit()
        else:
            print("Invalid input, please try again")

if __name__=='__main__':
    main()
