from controllers.usuario_controller import UsuarioController
from .menu_usuario import MenuUsuario
from .menu_livro import MenuLivro
from .menu_emprestimo import MenuEmprestimo
import utils.validar_inputs as inpt
import os

class Menu():
    @staticmethod
    def menu_usuario():
        while True:
            print("====== GERENCIAR USUÁRIOS ======")
            escolha = inpt.entrar_numero_inteiro("1 - Criar Usuário\n2 - Listar Usuários\n3 - Atualizar Usuário\n4 - Desativar Usuário\n5 - Listar Empréstimos Ativos\n0 - Voltar para o menu principal\nEscolha: ")
            match escolha:
                case 1: MenuUsuario.criar_usuario()
                case 2: MenuUsuario.listar_usuarios()
                case 3: MenuUsuario.atualizar_usuario()
                case 4: MenuUsuario.desativar_usuario()
                case 5: MenuUsuario.listar_emprestimos_ativos()
                case 0: return os.system('cls' if os.name == 'nt' else 'clear')
                case _: print("Escolha inválida.")
    @staticmethod
    def menu_emprestimo():
        while True:
            print("====== GERENCIAR EMPRÉSTIMOS ======")
            escolha = inpt.entrar_numero_inteiro("1 - Realizar Empréstimo\n2 - Registrar Devolução\n3 - Listar Empréstimos Ativos\n0 - Voltar para o menu principal\nEscolha: ")
            match escolha:
                case 1: MenuEmprestimo.realizar_emprestimo()
                case 2: MenuEmprestimo.registrar_devolucao()
                case 3: MenuEmprestimo.listar_emprestimos_ativos()
                case 0: return os.system('cls' if os.name == 'nt' else 'clear')
                case _: print("Escolha inválida.")
    @staticmethod
    def menu_livro():
        while True:
            print("====== GERENCIAR LIVROS ======")
            escolha = inpt.entrar_numero_inteiro("1 - Criar Livro\n2 - Listar Livros\n3 - Listar Livros Disponíveis\n4 - Atualizar Livro\n0 - Voltar para o menu principal\nEscolha: ")
            match escolha:
                case 1: MenuLivro.criar_livro()
                case 2: MenuLivro.listar_livros()
                case 3: MenuLivro.listar_livros_disponiveis()
                case 4: MenuLivro.atualizar_livro()
                case 0: return os.system('cls' if os.name == 'nt' else 'clear')
                case _: print("Escolha inválida.")
    @staticmethod
    def menu():
        while True:
            print("====== BIBLIOTECA ======")
            escolha = inpt.entrar_numero_inteiro("1 - Gerenciar Usuários\n2 - Gerenciar Empréstimos\n3 - Gerenciar Livros\n0 - Encerrar\nEscolha: ")
            match escolha:
                case 1: Menu.menu_usuario()
                case 2: Menu.menu_emprestimo()
                case 3: Menu.menu_livro()
                case 0: return print("Aplicação encerrada.")
                case _: print("Escolha inválida.")