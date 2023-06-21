from flask import Flask, request, jsonify, make_response
from connect import connect_to_database, close_database_connection, execute_query

app = Flask(__name__)
connection = None

# funzione per connettersi al database
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

# funzione per registrare un nuovo utente
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

# funzione per cambiare la password
@app.route('/changepass', methods=['POST'])
def change_password():
    '''
    Cambia la password.
    :return: esito del cambio della password
    '''
    username = request.form['username']
    old_password = request.form['old_password']
    new_password = request.form['new_password']
    result = execute_query(connection, "SELECT * FROM utente WHERE username = '" + username + "' AND password = '" + old_password + "'")
    if result:
        execute_query(connection, "UPDATE utente SET password = '" + new_password + "' WHERE username = '" + username + "'")
        response = make_response('Password changed successfully', 200)
    else:
        response = make_response('Invalid username or password', 401)
    return response

# funzione per eliminare l'utente
@app.route('/deleteuser', methods=['POST'])
def delete_user():
    '''
    Elimina l'utente.
    :return: esito dell'eliminazione dell'utente
    '''
    username = request.form['username']
    password = request.form['password']
    result = execute_query(connection, "SELECT * FROM utente WHERE username = '" + username + "' AND password = '" + password + "'")
    if result:
        execute_query(connection, "DELETE FROM utente INNER JOIN task ON utente.id = task.id_utente WHERE username = '" + username + "'")
        response = make_response('User deleted successfully', 200)
    else:
        response = make_response('Invalid username or password', 401)
    return response

# funzione per ottenere tutti i task di un utente
@app.route('/gettasks', methods=['POST'])
def get_tasks():
    '''
    Ottiene tutti i task di un utente.
    :return: task dell'utente
    '''
    username = request.form['username']
    password = request.form['password']
    result = execute_query(connection, "SELECT * FROM utente WHERE username = '" + username + "' AND password = '" + password + "'")
    if result:
        result = execute_query(connection, "SELECT * FROM task WHERE id_utente = " + str(result[0][0]))
        response = make_response(jsonify(result), 200)
    else:
        response = make_response('Invalid username or password', 401)
    return response

# funzione per aggiungere un task
@app.route('/addtask', methods=['POST'])
def add_task():
    '''
    Aggiunge un task.
    :return: esito dell'aggiunta del task
    '''
    username = request.form['username']
    password = request.form['password']
    title = request.form['title']
    description = request.form['description']
    date = request.form['date']
    result = execute_query(connection, "SELECT * FROM utente WHERE username = '" + username + "' AND password = '" + password + "'")
    if result:
        execute_query(connection, "INSERT INTO task (id_utente, titolo, descrizione, data) VALUES (" + str(result[0][0]) + ", '" + title + "', '" + description + "', '" + date + "')")
        response = make_response('Task added successfully', 201)
    else:
        response = make_response('Invalid username or password', 401)
    return response
    
# funzione per eliminare un task
@app.route('/deletetask', methods=['POST'])
def delete_task():
    '''
    Elimina un task.
    :return: esito dell'eliminazione del task
    '''
    username = request.form['username']
    password = request.form['password']
    title = request.form['title']
    result = execute_query(connection, "SELECT * FROM utente WHERE username = '" + username + "' AND password = '" + password + "'")
    if result:
        execute_query(connection, "DELETE FROM task WHERE id_utente = " + str(result[0][0]) + " AND titolo = '" + title + "'")
        response = make_response('Task deleted successfully', 200)
    else:
        response = make_response('Invalid username or password', 401)
    return response

# funzione per modificare un task
@app.route('/updatetask', methods=['POST'])
def update_task():
    '''
    Modifica un task.
    :return: esito della modifica del task
    '''
    username = request.form['username']
    password = request.form['password']
    old_title = request.form['old_title']
    new_title = request.form['new_title']
    new_description = request.form['new_description']
    new_date = request.form['new_date']
    result = execute_query(connection, "SELECT * FROM utente WHERE username = '" + username + "' AND password = '" + password + "'")
    if result:
        execute_query(connection, "UPDATE task SET titolo = '" + new_title + "', descrizione = '" + new_description + "', data = '" + new_date + "' WHERE id_utente = " + str(result[0][0]) + " AND titolo = '" + old_title + "'")
        response = make_response('Task updated successfully', 200)
    else:
        response = make_response('Invalid username or password', 401)
    return response

if __name__ == '__main__':
    connection = connect_to_database()  # Chiama la funzione per connettersi al database
    app.run()  # Avvia il server Flask
    close_database_connection(connection)  # Chiama la funzione per chiudere la connessione al database