import mysql.connector
from mysql.connector import errorcode
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
        CREATE TABLE IF NOT EXISTS Boats (
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
    query_boat = 'SELECT * FROM Boats'
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
    query_insert_boat = 'INSERT INTO Boats (boat, owner, captain, capacity, crew) VALUES (%s, %s, %s, %s, %s)'
    cur = connection.cursor()
    cur.execute(query_insert_boat,(boat, owner, captain, capacity, crew))
    connection.commit()
    connection.close()

def search(boat):
    connection = mysql.connector.connect(
        host="localhost",
        database="face_recognition_db",
        user="root",
        password=""
    )
    query_to_search = 'SELECT * FROM Boats WHERE boat LIKE %s'
    cur = connection.cursor()
    cur.execute(query_to_search, (f"%{boat}",))
    item_name = cur.fetchall()
    connection.close()
    return item_name

def delete_boat(boat):
    connection = mysql.connector.connect(
        host="localhost",
        database="face_recognition_db",
        user="root",
        password=""
    )
    query_delete_boat = 'DELETE FROM Boats WHERE boat = %s' # baka babaguhin yung name baka maging id
    cur = connection.cursor()
    cur.execute(query_delete_boat, (boat,))
    connection.commit()
    connection.close()

# def delete_boat(boat):
#     try:
#         connection = mysql.connector.connect(
#             host="localhost",
#             database="face_recognition_db",
#             user="root",
#             password=""
#         )
#         query_delete_boat = 'DELETE FROM Boats WHERE boat = %s' # baka babaguhin yung name baka maging id
#         cur = connection.cursor()
#         cur.execute(query_delete_boat, (boat,))
#         connection.commit()
#         connection.close()
#     except mysql.connector.Error as err:
#         if err.errno == errorcode.CR_SERVER_LOST:
#             print("Lost connection to MySQL server. Reconnecting...")
#             # You might want to attempt to reconnect here or handle it based on your application logic.
#         else:
#             print(f"Error: {err}")

def update_boat(new_owner, new_captain, new_capacity, new_crew, boat):
    connection = mysql.connector.connect(
        host="localhost",
        database="face_recognition_db",
        user="root",
        password=""
    )
    query_update_boat = 'UPDATE Boats SET owner = %s, captain = %s, capacity = %s, crew = %s WHERE boat = %s'
    cur = connection.cursor()
    cur.execute(query_update_boat, (new_owner, new_captain, new_capacity, new_crew, boat))
    connection.commit()
    connection.close()

def name_exists(boat):
    connection = mysql.connector.connect(
        host="localhost",
        database="face_recognition_db",
        user="root",
        password=""
    )
    query_name_exists = 'SELECT COUNT(*) FROM Boats WHERE boat = %s'
    cur = connection.cursor()
    cur.execute(query_name_exists, (boat,))
    result = cur.fetchone()
    connection.close()
    return result[0] > 0

create_table()