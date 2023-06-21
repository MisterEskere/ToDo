from flask import Flask, request, jsonify
from connect import connect_to_database, close_database_connection, execute_query

app = Flask(__name__)
connection = None

@app.route('/users', methods=['GET'])
def get_all_users():
    '''
    Restituisce tutti gli utenti presenti nel database.
    :return: lista di utenti
    '''
    return jsonify(execute_query(connection, "SELECT * FROM utente"))



if __name__ == '__main__':
    connection = connect_to_database()  # Chiama la funzione per connettersi al database
    app.run()  # Avvia il server Flask
    close_database_connection(connection)  # Chiama la funzione per chiudere la connessione al database