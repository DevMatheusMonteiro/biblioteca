from controllers.usuario_controller import UsuarioController
import utils.validar_inputs as inpt

class MenuUsuario():
    @staticmethod
    def criar_usuario():
        print("====== CADASTRAR USUÁRIO ======")
        nome_completo = inpt.entrar_texto("Nome completo: ").strip()
        data_nascimento = inpt.entrar_data("Data de Nascimento (YYYY-MM-DD): ")
        res = UsuarioController.criar_usuario(nome_completo=nome_completo, data_nascimento=data_nascimento)
        print(res)
    @staticmethod
    def listar_usuarios():
        print("====== LISTAR USUÁRIOS ======")
        res = UsuarioController.listar_usuarios()
        if type(res) == list:
            for usuario in res:
                print(usuario.__str__())
        else:
            print(res)
    @staticmethod
    def listar_emprestimos_ativos():
        print("====== LISTAR USUÁRIOS ======")
        id = inpt.entrar_numero_inteiro("ID do usuário: ")
        res = UsuarioController.listar_emprestimos_ativos(id)
        if type(res) == list:
            for emprestimo in res:
                print(emprestimo.__str__())
        else:
            print(res)
    @staticmethod
    def atualizar_usuario():
        print("====== ATUALIZAR USUÁRIO ======")
        id = inpt.entrar_numero_inteiro("ID do usuário: ")
        nome_completo = inpt.entrar_texto("Nome completo: ").strip()
        data_nascimento = inpt.entrar_data("Data de Nascimento (YYYY-MM-DD): ")
        res = UsuarioController.atualizar_usuario(id=id, nome_completo=nome_completo, data_nascimento=data_nascimento)
        print(res)
    @staticmethod
    def desativar_usuario():
        print("====== DESATIVAR USUÁRIO ======")
        id = inpt.entrar_numero_inteiro("ID do usuário: ")
        res = UsuarioController.desativar_usuario(id)
        print(res)