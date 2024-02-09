import mysql.connector
# from mysql.connector import Error

# try:
#     connection = mysql.connector.connect(
#         host="localhost",
#         database="face_recognition_db",
#         user="root",
#         password=""
#     )
#     if connection.is_connected():
#         print("CONNECTED")
# except Error as error:
#     print("The error is: {}".format(error))

# finally:
#     if connection.is_connected():
#         connection.close()
#         print("Connection CLOSE")

# def create_table():
#     try:
#         connection = mysql.connector.connect(
#             host="localhost",
#             database="face_recognition_db",
#             user="root",
#             password=""
#         )
#         query = '''
#             CREATE TABLE IF NOT EXISTS Passengers (
#             boat TEXT PRIMARY KEY,
#             owner TEXT,
#             captain TEXT,
#             capacity TEXT,
#             crew TEXT)'''
#         cur = connection.cursor()
#         cur.execute(query)
#         connection.commit()
#         cur.close()
#     except Error as error:
#         print("The error is: {}".format(error))
#     finally:
#         if connection.is_connected():
#             connection.close()
#             print("Connection CLOSE")

def create_table():
    connection = mysql.connector.connect(
        host="localhost",
        database="face_recognition_db",
        user="root",
        password=""
    )
    query = '''
        CREATE TABLE IF NOT EXISTS Passengers (
        boat VARCHAR(255) PRIMARY KEY,
        owner TEXT,
        captain TEXT,
        capacity TEXT,
        crew TEXT)'''
    cur = connection.cursor()
    cur.execute(query)
    connection.commit()
    connection.close()

def fetch_boat():
    connection = mysql.connector.connect(
        host="localhost",
        database="face_recognition_db",
        user="root",
        password=""
    )
    query_boat = 'SELECT * FROM Passengers'
    cur = connection.cursor()
    cur.execute(query_boat)
    boats = cur.fetchall()
    connection.close()
    return boats

def insert_boat(boat, owner, captain, capacity, crew):
    connection = mysql.connector.connect(
        host="localhost",
        database="face_recognition_db",
        user="root",
        password=""
    )
    query_insert_boat = 'INSERT INTO Passengers (boat, owner, captain, capacity, crew) VALUES (?, ?, ?, ?, ?)',(boat, owner, captain, capacity, crew)
    cur = connection.cursor()
    cur.execute(query_insert_boat)
    connection.commit()
    connection.close()

def delete_boat(name):
    connection = mysql.connector.connect(
        host="localhost",
        database="face_recognition_db",
        user="root",
        password=""
    )
    query_delete_boat = 'DELETE FROM Passengers WHERE name = ?', (name,) # baka babaguhin yung name baka maging id
    cur = connection.cursor()
    cur.execute(query_delete_boat)
    connection.commit()
    connection.close()

def update_boat(new_owner, new_captain, new_capacity, new_crew, boat):
    connection = mysql.connector.connect(
        host="localhost",
        database="face_recognition_db",
        user="root",
        password=""
    )
    query_update_boat = 'UPDATE Passengers SET owner = ?, captain = ?, capacity = ?, crew = ? WHERE boat = ?', (new_owner, new_captain, new_capacity, new_crew, boat)
    cur = connection.cursor()
    cur.execute(query_update_boat)
    connection.commit()
    connection.close()

def name_exists(name):
    connection = mysql.connector.connect(
        host="localhost",
        database="face_recognition_db",
        user="root",
        password=""
    )
    query_name_exists = 'SELECT COUNT(*) FROM Passengers WHERE name = ?', (name,)
    cur = connection.cursor()
    cur.execute(query_name_exists)
    result = cur.fetchone()
    connection.close()
    return result[0] > 0

create_table()