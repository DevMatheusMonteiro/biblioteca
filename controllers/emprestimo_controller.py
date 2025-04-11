from services.emprestimo_service import EmprestimoService
from app_error import AppError

class EmprestimoController():
    @staticmethod
    def realizar_emprestimo(usuario_id, livro_id):
        try:
            EmprestimoService.realizar_emprestimo(usuario_id=usuario_id, livro_id=livro_id)
            return "Empréstimo realizado com sucesso."
        except AppError as e:
            return e.message
        except Exception as e:
            return f"Um erro inesperado ocorreu: {e}."
    @staticmethod
    def registrar_devolucao(usuario_id, livro_id):
        try:
            EmprestimoService.registrar_devolucao(usuario_id=usuario_id, livro_id=livro_id)
            return "Devolução realizada com sucesso."
        except AppError as e:
            return e.message
        except Exception as e:
            return f"Um erro inesperado ocorreu: {e}."
    @staticmethod
    def listar_emprestimos_ativos():
        try:
            return EmprestimoService.listar_emprestimos_ativos()
        except AppError as e:
            return e.message
        except Exception as e:
            return f"Um erro inesperado ocorreu: {e}."
