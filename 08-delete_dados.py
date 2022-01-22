import sqlite3

conn = sqlite3.connect("clientes.db")
cursor = conn.cursor()

id_cliente = 8

cursor.execute("""
DELETE FROM clientes
WHERE id = ?
""", (id_cliente,))

conn.commit()

print('Registro excluido com sucesso.')

conn.close()
