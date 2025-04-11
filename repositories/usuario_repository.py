from database_config_sqlalchemy import session
from models.usuario import Usuario
from models.emprestimo import Emprestimo

class UsuarioRepository:
    @staticmethod
    def criar_usuario(usuario):
        session.add(usuario)
        session.commit()
    @staticmethod
    def listar_usuarios():
        return session.query(Usuario).filter_by(ativo=True).all()
    @staticmethod
    def buscar_por_id(id):
        return session.get(Usuario, id)
    @staticmethod
    def contar_emprestimos_ativos(id):
        return session.query(Emprestimo).filter_by(usuario_id=id, data_devolucao=None).count()
    @staticmethod
    def listar_emprestimos_ativos(id):
        return session.query(Emprestimo).filter_by(usuario_id=id, data_devolucao=None).all()
    @staticmethod
    def atualizar_usuario():
        session.commit()