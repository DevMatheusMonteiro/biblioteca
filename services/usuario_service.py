from datetime import datetime
from models.usuario import Usuario
from repositories.usuario_repository import UsuarioRepository
from app_error import AppError

class UsuarioService:
    @staticmethod
    def criar_usuario(nome_completo, data_nascimento_str):
        if nome_completo == None or nome_completo.strip():
            raise AppError("Erro: nome nulo ou vazio.")
        if data_nascimento_str == None or data_nascimento_str.strip():
            raise AppError("Erro: data de nascimento nula ou vazia.")
        data_nascimento = datetime.strptime(data_nascimento_str, "%Y-%m-%d")
        usuario = Usuario(nome_completo=nome_completo, data_nascimento=data_nascimento)
        UsuarioRepository.criar_usuario(usuario)
    @staticmethod
    def listar_usuarios():
        return UsuarioRepository.listar_usuarios()
    @staticmethod
    def atualizar_usuario(id, nome_completo=None, data_nascimento_str=None):
        usuario = UsuarioRepository.buscar_por_id(id)
        if not usuario:
            raise AppError("Erro: usuário não encontrado.")
        if nome_completo != None and nome_completo.strip() != "":
            usuario.nome_completo = nome_completo
        if data_nascimento != None and data_nascimento.strip() != "":
            data_nascimento = datetime.strptime(data_nascimento_str, "%Y-%m-%d")
            usuario.data_nascimento = data_nascimento
        UsuarioRepository.atualizar_usuario()
    @staticmethod
    def desativar_usuario(id):
        usuario = UsuarioRepository.buscar_por_id(id)
        if not usuario:
            raise AppError("Erro: usuário não encontrado.")
        usuario.ativo = False
        UsuarioRepository.atualizar_usuario()