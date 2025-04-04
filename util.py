import pandas as pd
import database_config_sqlite as db
import os

def ler_csv(arquivo):
    try:
        df = pd.read_csv(os.path.abspath(os.path.join(__file__, "..", "dados", f"{arquivo}.csv")))
        return df
    except Exception as e:
        print(f"Erro ao tentar ler o arquivo csv: {e}")
def escrever_json(df, arquivo):
    try:
        df.to_json(os.path.abspath(os.path.join(__file__, "..", "dados_json", f"{arquivo}.json")), orient="records", indent=2)
    except Exception as e:
        print(f"Erro ao tentar ler o arquivo csv: {e}")
def inserir_dados(df, tabela):
    try:
        conn = db.conectar()
        df.to_sql(tabela, conn, if_exists="replace", index=False)
    except Exception as e:
        print(f"Erro ao inserir dados: {e}")
    finally:
        db.desconectar(conn)
def renomear_coluna(df, colunas):
    return df.rename(columns=colunas)
def consultar_dados(consulta):
    try:
        conn = db.conectar()
        return pd.read_sql(consulta, conn)
    except Exception as e:
        print(f"Erro ao consultar dados: {e}")
    finally:
        db.desconectar(conn)