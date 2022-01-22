import sqlite3

conn = sqlite3.connect("clientes.db")
cursor = conn.cursor()

id_cliente = 9
novo_nome = 'maisa'
novo_criado_em ='2014-06-11'

cursor.execute("""
UPDATE clientes
SET nome = ?, criado_em = ?
WHERE id = ?
""", (novo_nome, novo_criado_em, id_cliente))

conn.commit()

print('Dados Atulizados com sucesso.')

conn.close()
