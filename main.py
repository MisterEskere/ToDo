from flask import Flask, request, jsonify, make_response
from connect import connect_to_database, close_database_connection, execute_query

app = Flask(__name__)
connection = None

@app.route('/login', methods=['POST'])
def login():
    '''
    Esegue il login.
    :return: esito del login
    '''
    username = request.form['username']
    password = request.form['password']
    result = execute_query(connection, "SELECT * FROM utente WHERE username = '" + username + "' AND password = '" + password + "'")
    if result:
        response = make_response('Login successful', 200)
    else:
        response = make_response('Invalid username or password', 401)
    return response

@app.route('/signin', methods=['POST'])
def signin():
    '''
    Esegue la registrazione.
    :return: esito della registrazione
    '''
    username = request.form['username']
    password = request.form['password']
    result = execute_query(connection, "SELECT * FROM utente WHERE username = '" + username + "'")
    if result:
        response = make_response('Username already exists', 409)
    else:
        execute_query(connection, "INSERT INTO utente (username, password) VALUES ('" + username + "', '" + password + "')")
        response = make_response('Signin successful', 201)
    return response

if __name__ == '__main__':
    connection = connect_to_database()  # Chiama la funzione per connettersi al database
    app.run()  # Avvia il server Flask
    close_database_connection(connection)  # Chiama la funzione per chiudere la connessione al database