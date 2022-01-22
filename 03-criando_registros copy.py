import sqlite3

conn = sqlite3.connect("clientes.db")
cursor = conn.cursor()

cursor.execute("""
INSERT INTO clientes (nome, idade, cpf, email, fone, cidade, uf, criado_em)
VALUES('Regis', 35, '00000000000', 'regis@email.com', '11-98765-4321', 'Sao Paulo', 'SP', '2022-01-21' )
""")

cursor.execute("""
INSERT INTO clientes (nome, idade, cpf, email, fone, cidade, uf, criado_em)
VALUES('Aloisio', 87, '11111111111', 'aloisio@email.com', '11-98765-4322', 'Port Alegre', 'RS', '2022-01-22' )
""")

cursor.execute("""
INSERT INTO clientes (nome, idade, cpf, email, fone, cidade, uf, criado_em)
VALUES('Bruna', 21, '22222222222', 'bruna@email.com', '11-98765-4323', 'Rio de Janeiro', 'rj', '2022-01-22' )
""")

cursor.execute("""
INSERT INTO clientes (nome, idade, cpf, email, fone, cidade, uf, criado_em)
VALUES('Matheus', 19, '33333333333', 'matheus@email.com', '11-98765-4324', 'Campinas', 'SP', '2022-01-21' )
""")

cursor.execute("""
INSERT INTO clientes (nome, idade, cpf, email, fone, cidade, uf, criado_em)
VALUES('maicke', 20, '44444444444', 'maicke@email.com', '11-98765-4325', 'Sao Paulo', 'SP', '2022-01-22' )
""")

conn.commit()

print('Dados inseridos com sucesso.')

conn.close()
