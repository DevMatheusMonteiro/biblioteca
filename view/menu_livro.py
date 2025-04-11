from controllers.livro_controller import LivroController
import utils.validar_inputs as inpt

class MenuLivro():
    @staticmethod
    def criar_livro():
        print("====== CADASTRAR LIVRO ======")
        titulo = inpt.entrar_texto("Nome completo: ").strip()
        isbn = inpt.entrar_texto("ISBN: ").strip()
        genero = inpt.entrar_texto("Gênero: ").strip()
        data_publicacao = inpt.entrar_data("Data de Publicação: ")
        qtd_paginas = inpt.entrar_numero_inteiro("Quatidade de páginas: ")
        estoque = inpt.entrar_numero_inteiro("Quantidade de livros em estoque: ")
        res = LivroController.criar_livro(titulo=titulo, isbn=isbn, genero=genero, data_publicacao=data_publicacao, qtd_paginas=qtd_paginas, estoque=estoque)
        print(res)
    @staticmethod
    def listar_livros():
        print("====== LISTAR LIVROS ======")
        res = LivroController.listar_livros()
        if type(res) == list:
            for livro in res:
                print(livro.__str__())
        else:
            print(res)
    @staticmethod
    def listar_livros_disponiveis():
        print("====== LISTAR LIVROS DISPONÍVEIS ======")
        res = LivroController.listar_livros_disponiveis()
        if type(res) == list:
            for livro in res:
                print(livro.__str__())
        else:
            print(res)
    @staticmethod
    def atualizar_livro():
        id = inpt.entrar_numero_inteiro("ID do livro: ")
        titulo = inpt.entrar_texto("Nome completo: ").strip()
        isbn = inpt.entrar_texto("ISBN: ").strip()
        genero = inpt.entrar_texto("Gênero: ").strip()
        data_publicacao = inpt.entrar_data("Data de Publicação: ")
        qtd_paginas = inpt.entrar_numero_inteiro("Quatidade de páginas: ")
        estoque = inpt.entrar_numero_inteiro("Quantidade de livros em estoque: ")
        res = LivroController.atualizar_livro(id=id, titulo=titulo, isbn=isbn, genero=genero, data_publicacao=data_publicacao, qtd_paginas=qtd_paginas, estoque=estoque)
        print(res)