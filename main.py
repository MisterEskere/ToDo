from flask import Flask, request, jsonify
from mysql.connector import connect, Error

app = Flask(__name__)

db_connection = None

# Configurazione del database
db_config = {
    'host': 'localhost',  # Indirizzo del database
    'user': 'root',  # Nome utente del database
    'password': 'x',  # Password del database
    'database': 'ToDo'  # Nome del database
}

def connect_to_database():
    global db_connection
    try:
        db_connection = connect(**db_config)  # Connessione al database MariaDB utilizzando le informazioni di configurazione
        print("Connessione al database avvenuta con successo.")
    except Error as e:
        print("Errore durante la connessione al database:", e)
        db_connection = None

if __name__ == '__main__':
    connect_to_database()  # Chiama la funzione per connettersi al database