from services.usuario_service import UsuarioService
from app_error import AppError

class UsuarioController():
    @staticmethod
    def criar_usuario(nome_completo, data_nascimento):
        try:
            UsuarioService.criar_usuario(nome_completo=nome_completo, data_nascimento=data_nascimento)
            return "Usuário adicionado com sucesso."
        except AppError as e:
            return e.message
        except Exception as e:
            return f"Um erro inesperado ocorreu: {e}."
    @staticmethod
    def listar_usuarios():
        try:
            return UsuarioService.listar_usuarios()
        except AppError as e:
            return e.message
        except Exception as e:
            return f"Um erro inesperado ocorreu: {e}."
    @staticmethod
    def atualizar_usuario(id, nome_completo, data_nascimento):
        try:
            UsuarioService.atualizar_usuario(id=id, nome_completo=nome_completo, data_nascimento=data_nascimento)
            return "Usuário atualizado com sucesso."
        except AppError as e:
            return e.message
        except Exception as e:
            return f"Um erro inesperado ocorreu: {e}."
    @staticmethod
    def desativar_usuario(id):
        try:
            UsuarioService.desativar_usuario(id)
            return "Usuário desativado com sucesso."
        except AppError as e:
            return e.message
        except Exception as e:
            return f"Um erro inesperado ocorreu: {e}."