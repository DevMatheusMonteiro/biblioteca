from datetime import datetime
from models.emprestimo import Emprestimo
from repositories.emprestimo_repository import EmprestimoRepository
from repositories.usuario_repository import UsuarioRepository
from repositories.livro_repository import LivroRepository
from app_error import AppError

class EmprestimoService:
    @staticmethod
    def realizar_emprestimo(usuario_id: int, livro_id: int):
        usuario = UsuarioRepository.buscar_por_id(usuario_id)
        livro = LivroRepository.buscar_por_id(livro_id)
        if not usuario:
            raise AppError("Erro: usuário não encontrado.")
        if not livro:
            raise AppError("Erro: livro não encontrado.")
        qtd_emprestimos = UsuarioRepository.contar_emprestimos_ativos(usuario.id)
        if qtd_emprestimos == 5:
            raise AppError("Erro: limite de 5 livros emprestados atingido.")
        if livro.estoque == 0:
            raise AppError("Erro: estoque esgotado.")
        emprestimo_ativo = EmprestimoRepository.buscar_ativo(usuario_id, livro_id)
        if emprestimo_ativo:
            raise AppError("Erro: usuário ainda possui um empréstimo ativo deste livro.")
        livro.estoque -= 1
        emprestimo = Emprestimo(usuario_id=usuario_id, livro_id=livro_id)
        EmprestimoRepository.criar_emprestimo(emprestimo)
    @staticmethod
    def registrar_devolucao(usuario_id, livro_id):
        emprestimo = EmprestimoRepository.buscar_ativo(usuario_id, livro_id)
        if not emprestimo:
            raise AppError("Erro: empréstimo não encontrado.")
        livro = LivroRepository.buscar_por_id(livro_id)
        livro.estoque += 1
        emprestimo.data_devolucao = datetime.now()
        EmprestimoRepository.atualizar_emprestimo()
    @staticmethod
    def listar_emprestimos_ativos():
        return EmprestimoRepository.listar_emprestimos_ativos()