import sqlite3

conn = sqlite3.connect("clientes.db")

print('Banco conectado com sucesso.')

conn.close()