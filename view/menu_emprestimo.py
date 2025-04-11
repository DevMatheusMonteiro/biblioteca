from controllers.emprestimo_controller import EmprestimoController
import utils.validar_inputs as inpt

class MenuEmprestimo():
    @staticmethod
    def realizar_emprestimo():
        print("====== REALIZAR EMPRÉSTIMO ======")
        usuario_id = inpt.entrar_numero_inteiro("ID do usuário: ")
        livro_id = inpt.entrar_numero_inteiro("ID do livro: ")
        res = EmprestimoController.realizar_emprestimo(usuario_id=usuario_id, livro_id=livro_id)
        print(res)
    @staticmethod
    def registrar_devolucao():
        print("====== REGISTRAR DEVOLUÇÃO ======")
        usuario_id = inpt.entrar_numero_inteiro("ID do usuário: ")
        livro_id = inpt.entrar_numero_inteiro("ID do livro: ")
        res = EmprestimoController.registrar_devolucao(usuario_id=usuario_id, livro_id=livro_id)
        print(res)
    @staticmethod
    def listar_emprestimos_ativos():
        print("====== LISTA TODOS OS EMPRESTIMOS ATIVOS ======")
        res = EmprestimoController.listar_emprestimos_ativos()
        if type(res) == list:
            for emprestimo in res:
                print(emprestimo.__str__())
        else:
            print(res)