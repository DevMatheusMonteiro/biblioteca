import sqlite3
import os

def conectar():
    try:
        conn = sqlite3.connect(os.path.abspath(os.path.join(__file__, "..", "database.db")))
        return conn
    except Exception as e:
        print(f"Erro ao conecta com banco de dados: {e}")
def desconectar(conn):
    if conn is not None:
        conn.close()