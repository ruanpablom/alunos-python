from config import db

try:
  conn = db.connect()
  cursor = conn.cursor()
  cursor.execute('''
                CREATE TABLE IF NOT EXISTS aluno (id SERIAL PRIMARY KEY, nome VARCHAR(255), turma INT, notas FLOAT[], faltas INT)
                ''')
  conn.commit()
  cursor.close()
  db.close(conn)
  print("Tabela aluno criada com sucesso!")
except Exception as e:
  print(e)
  db.close(conn)