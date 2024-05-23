import os
import psycopg2
from dotenv import load_dotenv

load_dotenv()


def connect():
    conn = None
    try:
        conn = psycopg2.connect(
            host=os.getenv("DB_HOST"),
            database=os.getenv("DB_NAME"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASS"),
            port=os.getenv("DB_PORT")
        )
        return conn
    except Exception as e:
        print("Não foi possível conectar ao banco de dados!")
        raise e



def close(conexao):
    try:
        conexao.close()
    except Exception as e:
        print("Erro ao fechar conexão: ", e)
        raise e