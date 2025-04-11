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
        res = UsuarioController.listar_usuarios()
        if type(res) == list:
            for usuario in UsuarioController.listar_usuarios():
                print(usuario.__str__())
        else:
            print(res)