from datetime import datetime

def entrar_texto(mensagem):
    while True:
        texto = input(mensagem)
        if texto != None or texto.strip() != "":
            return texto
        print("Erro: texto nulo ou vazio.")
def entrar_numero_inteiro(mensagem):
    while True:
        try:
            numero_inteiro = int(input(mensagem))
            return numero_inteiro
        except ValueError:
            print("Erro: número inválido.")
def entrar_data(mensagem):
    while True:
        try:
            data = datetime.strptime(input(mensagem), "%Y-%m-%d")
            return data
        except ValueError:
            print("Erro: número inválido.")