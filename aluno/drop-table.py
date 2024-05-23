from config import db

try:
  conn = db.connect()
  cursor = conn.cursor()
  cursor.execute('''
                DROP TABLE aluno
                ''')
  conn.commit()
  cursor.close()
  db.close(conn)
except Exception as e:
  print(e)
  db.close(conn)