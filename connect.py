from mysql.connector import Error, connect

db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'x',
    'database': 'ToDo'
}

def connect_to_database():
    '''
    Crea una connessione al database.
    :return: connessione al database
    '''
    try:
        db_connection = connect(**db_config)
        print("Connessione al database avvenuta con successo.")
    except Error as e:
        print("Errore durante la connessione al database:", e)
        db_connection = None

    return db_connection

def close_database_connection(db_connection):
    '''
    Chiude la connessione al database.
    :param db_connection: connessione al database
    '''
    if db_connection:
        db_connection.close()
        print("Connessione al database chiusa.")


def execute_query(db_connection,query):
    '''
    Esegue una query sul database.
    :param db_connection: connessione al database
    :param query: query da eseguire
    :return: risultato della query
    '''
    try:
        cursor = db_connection.cursor()
        cursor.execute(query)
        result = cursor.fetchall()
        cursor.close()
        return result
    except Error as e:
        print("Errore durante l'esecuzione della query:", e)
        return None
