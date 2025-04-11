from database_config_sqlalchemy import Base, sql, orm

class Usuario(Base):
    __tablename__ = 'usuario'

    id = sql.Column(sql.Integer, primary_key=True, autoincrement=True)
    nome_completo = sql.Column(sql.String, nullable=False)
    data_nascimento = sql.Column(sql.DateTime, nullable=False)
    ativo = sql.Column(sql.Boolean, default=True)

    emprestimos = orm.relationship("Emprestimo", back_populates="usuario")

    def __str__(self):
        return f"ID - {self.id} | Nome Completo - {self.nome_completo} | Data de Nascimento - {self.data_nascimento}"