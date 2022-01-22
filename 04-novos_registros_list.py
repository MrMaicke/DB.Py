import sqlite3

conn = sqlite3.connect("clientes.db")
cursor = conn.cursor()

lista = [(
    'Fabio', 23, '55555555555', 'fabio@email.com', '11-98765-4325', 'Belo Horizonte', 'MG', '2022-01-22'),
    ('Joao', 21, '66666666666', 'joao@email.com', '11-98765-4326', 'Sao Paulo', 'SP', '2022-01-22' ),
    ('Xavier', 24, '77777777777', 'xavier@email.com', '11-98765-4327', 'Campinas', 'SP', '2022-01-22' )]

cursor.executemany("""
INSERT INTO clientes (nome, idade, cpf, email, fone, cidade, uf, criado_em)
VALUES (?,?,?,?,?,?,?,?)
""", lista)

conn.commit()

print('Dados inseridos com sucesso.')

conn.close()
