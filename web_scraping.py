from urllib import request
from bs4 import BeautifulSoup
from datetime import datetime

def formatar_data(data):
    try:
        return datetime.strptime(data, '%d-%m-%Y').strftime('%Y-%m-%d')
    except:
        return f"{data}-01-01"
def parser_html():
    lp = request.urlopen("https://pedrovncs.github.io/livrariapython/livros.html").read()
    soup = BeautifulSoup(lp, "html.parser")
    itens = soup.find_all("li", class_="list-group-item")
    livros = []
    autores = []
    livro_autor = []
    for item in itens:
        livro = {}
        livro["id"] = len(livros) + 1
        livro["titulo"] = item.find("h5").text.strip()
        autores_livro = []
        for p in item.find_all("p"):
            if "ISBN" in p.text:
                livro["isbn"] = p.text.split(":")[1].strip()
            if "Gênero" in p.text:
                livro["genero"] = p.text.split(":")[1].strip()
            if "Autor(es)" in p.text:
                for autor in p.text.split(":")[1].strip().split(","):
                    autores_livro.append({"nome": autor.strip()})
            if "País de Nascimento" in p.text:
                for i, pais in enumerate(p.text.split(":")[1].strip().split(",")):
                    autores_livro[i]["pais"] = pais.strip()
            if "Data de publicação" in p.text:
                livro["data_publicacao"] = formatar_data(p.text.split(":")[1].strip())
            if "Páginas" in p.text:
                livro["qtd_paginas"] = p.text.split(":")[1].strip()
            if "Quantidade Disponível" in p.text:
                livro["estoque"] = p.text.split(":")[1].strip()
        livros.append(livro)
        for autor in autores_livro:
            autor_id = len(autores) + 1
            autores.append({"id": autor_id, **autor})
            livro_autor.append({"livro_id": livro["id"], "autor_id": autor_id})
    return (livros, autores, livro_autor)