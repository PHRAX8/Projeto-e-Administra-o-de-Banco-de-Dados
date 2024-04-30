import psycopg2

conn = psycopg2.connect(
    dbname="atividades_db",
    user="postgres",
    password="postgres",
    host="127.0.0.1",
    port="5432"
)

cur = conn.cursor()

#Inserir uma atividade em algum projeto;

sql = "INSERT INTO atividade (descricao, projeto, data_inicio, data_fim) VALUES (%s, %s, %s, %s)"
val = ("ES - Atividade 3", 4, "2024-05-17", "2024-12-05")
cur.execute(sql, val)

conn.commit()

#Atualizar o líder de algum projeto;

sql = "UPDATE projeto SET responsavel = %s WHERE codigo = %s"
val = (4, 3)
cur.execute(sql, val)

conn.commit()

#Listar todos os projetos e suas atividades;

cur.execute("SELECT * FROM projeto ORDER BY codigo")

rows = cur.fetchall()
for row in rows:
    print(row)

cur.execute("SELECT * FROM atividade ORDER BY codigo")

rows = cur.fetchall()
for row in rows:
    print(row)

cur.close()
conn.close()