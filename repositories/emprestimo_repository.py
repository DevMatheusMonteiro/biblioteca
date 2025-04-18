from database_config_sqlalchemy import session
from models.emprestimo import Emprestimo

class EmprestimoRepository:
    @staticmethod
    def criar_emprestimo(emprestimo):
        session.add(emprestimo)
        session.commit()
    @staticmethod
    def buscar_ativo(usuario_id: int, livro_id: int):
        return session.query(Emprestimo).filter_by(usuario_id=usuario_id, livro_id=livro_id, data_devolucao=None).first()
    @staticmethod
    def listar_emprestimos_ativos():
        return session.query(Emprestimo).filter_by(data_devolucao=None).all()
    @staticmethod
    def atualizar_emprestimo():
        session.commit()