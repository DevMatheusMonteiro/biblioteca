from datetime import datetime
from models.usuario import Usuario
from repositories.usuario_repository import UsuarioRepository
from app_error import AppError

class UsuarioService:
    @staticmethod
    def criar_usuario(nome_completo, data_nascimento):
        if nome_completo == None or nome_completo.strip() == "":
            raise AppError("Erro: nome nulo ou vazio.")
        if data_nascimento == None:
            raise AppError("Erro: data de nascimento nula.")
        usuario = Usuario(nome_completo=nome_completo, data_nascimento=data_nascimento)
        UsuarioRepository.criar_usuario(usuario)
    @staticmethod
    def listar_usuarios():
        return UsuarioRepository.listar_usuarios()
    @staticmethod
    def atualizar_usuario(id, nome_completo=None, data_nascimento=None):
        usuario = UsuarioRepository.buscar_por_id(id)
        if not usuario:
            raise AppError("Erro: usuário não encontrado.")
        usuario.nome_completo = nome_completo if nome_completo != None and nome_completo.strip() != "" else usuario.nome_completo
        usuario.data_nascimento = data_nascimento if data_nascimento != None else usuario.data_nascimento
        UsuarioRepository.atualizar_usuario()
    @staticmethod
    def desativar_usuario(id):
        usuario = UsuarioRepository.buscar_por_id(id)
        if not usuario:
            raise AppError("Erro: usuário não encontrado.")
        usuario.ativo = False
        UsuarioRepository.atualizar_usuario()
    @staticmethod
    def listar_emprestimos_ativos(id):
        return UsuarioRepository.listar_emprestimos_ativos(id)