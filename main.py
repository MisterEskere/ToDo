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
