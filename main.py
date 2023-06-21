from flask import Flask, request, jsonify
from mysql.connector import connect, Error
from connect import connect_to_database, close_database_connection

app = Flask(__name__)

if __name__ == '__main__':
    connect_to_database()  # Chiama la funzione per connettersi al database
    close_database_connection()  # Chiama la funzione per chiudere la connessione al database