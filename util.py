import pandas as pd
import database_config as db
import os

def ler_csv(arquivo):
    try:
        df = pd.read_csv(os.path.abspath(os.path.join(__file__, "..", "dados", f"{arquivo}.csv")))
        return df
    except Exception as e:
        print(f"Erro ao tentar ler o arquivo csv: {e}")
def inserir_dados(df, tabela):
    try:
        conn = db.conectar()
        df.to_sql(tabela, conn, if_exists="append", index=False)
    except Exception as e:
        print(f"Erro ao inserir dados: {e}")
    finally:
        db.desconectar(conn)
def renomear_coluna(df, colunas):
    return df.rename(columns=colunas)