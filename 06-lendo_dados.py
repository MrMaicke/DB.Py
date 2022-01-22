import sqlite3

conn = sqlite3.connect("clientes.db")
cursor = conn.cursor()

cursor.execute("""
SELECT * FROM clientes
""")

for linha in cursor.fetchall():
    print(linha)

conn.close()
