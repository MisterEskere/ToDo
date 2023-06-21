from mysql.connector import Error, connect

db_connection = None

db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'x',
    'database': 'ToDo'
}

def connect_to_database():
    global db_connection
    try:
        db_connection = connect(**db_config)
        print("Connessione al database avvenuta con successo.")
    except Error as e:
        print("Errore durante la connessione al database:", e)
        db_connection = None

def close_database_connection():
    global db_connection
    if db_connection:
        db_connection.close()
        print("Connessione al database chiusa.")