from database_config_sqlalchemy import sql, orm, Base

class Emprestimo(Base):
    __tablename__ = 'emprestimo'

    data_emprestimo = sql.Column(sql.DateTime, nullable=False, default=sql.func.now())
    data_devolucao = sql.Column(sql.DateTime)
    usuario_id = sql.Column(sql.Integer, sql.ForeignKey('usuario.id'), primary_key=True)
    livro_id = sql.Column(sql.Integer, sql.ForeignKey('livro.id'), primary_key=True)

    usuario = orm.relationship("Usuario", back_populates="emprestimos")
    livro = orm.relationship("Livro", back_populates="emprestimos")

    def __str__(self):
        return f"Data de Empréstimo - {self.data_emprestimo} | Data de Devolução - {self.data_devolucao if self.data_devolucao != None else "ainda não devolvido"} | Usuário: {self.usuario.__str__()} | Livro: {self.livro.__str__()}"