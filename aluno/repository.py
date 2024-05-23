import psycopg2.extras
from config import db

def insert_aluno(aluno):
    conn = None
    try:
        conn = db.connect()
        cursor = conn.cursor()
        cursor.execute('INSERT INTO aluno (nome, turma, notas, faltas) VALUES (%s, %s, %s, %s)', (aluno["nome"], aluno["turma"], aluno["notas"], aluno["faltas"]))
        conn.commit()
        db.close(conn)
    except Exception as e:
        print("Erro ao inserir aluno!")
        if conn:
            db.close(conn)

def select_alunos():
    conn = None
    try:
        conn = db.connect()
        cursor = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor) 
        cursor.execute('SELECT * FROM aluno')
        alunos = cursor.fetchall()
        cursor.close()
        db.close(conn)
        return alunos
    except Exception as e:
        print("Erro ao buscar alunos!")
        if conn:
            db.close(conn)
        return None

def select_aluno(id):
    conn = None
    try:
        conn = db.connect()
        cursor = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor) 
        cursor.execute('SELECT * FROM aluno WHERE id = %s', (id,))
        aluno = cursor.fetchone()
        cursor.close()
        db.close(conn)
        return aluno
    except Exception as e:
        print("Erro ao buscar aluno!")
        if conn:
            db.close(conn)
        return None

def update_nome_aluno(id, nome):
    conn = None
    try:
        conn = db.connect()
        cursor = conn.cursor()
        cursor.execute('UPDATE aluno SET nome = %s WHERE id = %s', (nome, id))
        conn.commit()
        cursor.close()
        db.close(conn)
        print("Nome do aluno atualizado com sucesso!")
    except Exception as e:
        print("Erro ao atualizar nome do aluno!")
        if conn:
            db.close(conn)

def update_turma_aluno(id, turma):
    conn = None
    try:
        conn = db.connect()
        cursor = conn.cursor()
        cursor.execute('UPDATE aluno SET turma = %s WHERE id = %s', (turma, id))
        conn.commit()
        cursor.close()
        db.close(conn)
        print("Turma do aluno atualizada com sucesso!")
    except Exception as e:
        print("Erro ao atualizar turma do aluno!")
        if conn:
            db.close(conn)

def insert_nota_aluno(id, nota):
    conn = None
    try:
        conn = db.connect()
        cursor = conn.cursor()
        cursor.execute('UPDATE aluno SET notas = array_append(notas, %s) WHERE id = %s', (nota, id))
        conn.commit()
        cursor.close()
        db.close(conn)
        print("Nota do aluno inserida com sucesso!")
    except Exception as e:
        print("Erro ao inserir nota do aluno!")
        if conn:
            db.close(conn)

def insert_falta_aluno(id, faltas):
    conn = None
    try:
        conn = db.connect()
        cursor = conn.cursor()
        cursor.execute('UPDATE aluno SET faltas = faltas + %s WHERE id = %s', (faltas, id))
        conn.commit()
        cursor.close()
        db.close(conn)
        print("Falta do aluno inserida com sucesso!")
    except Exception as e:
        print("Erro ao inserir falta do aluno!")
        if conn:
            db.close(conn)

def delete_aluno(id):
    conn = None
    try:
        conn = db.connect()
        cursor = conn.cursor()
        cursor.execute('DELETE FROM aluno WHERE id = %s', (id,))
        conn.commit()
        cursor.close()
        db.close(conn)
        print("Aluno deletado com sucesso!")
    except Exception as e:
        print("Erro ao deletar aluno!")
        if conn:
            db.close(conn)
