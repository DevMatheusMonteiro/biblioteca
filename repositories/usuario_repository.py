from database_config_sqlalchemy import session
from models.usuario import Usuario
from models.emprestimo import Emprestimo

class UsuarioRepository:
    @staticmethod
    def adicionar(usuario):
        session.add(usuario)
        session.commit()
    @staticmethod
    def listar_todos():
        return session.query(Usuario).all()
    @staticmethod
    def buscar_por_id(usuario_id: int):
        return session.get(Usuario, usuario_id)
    @staticmethod
    def contar_emprestimos_ativos(usuario_id: int):
        return session.query(Emprestimo).filter_by(usuario_id=usuario_id, data_devolucao=None).count()