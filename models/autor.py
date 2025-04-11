from database_config_sqlalchemy import Base, sql, orm
from .livro_autor import livro_autor

class Autor(Base):
    __tablename__ = "autor"

    id = sql.Column(sql.Integer, primary_key=True, autoincrement=True)
    nome = sql.Column(sql.String, nullable=False)

    livros = orm.relationship("Livro", secondary=livro_autor, back_populates="autores")

    def __str__(self):
        return f"ID - {self.id} | Nome - {self.nome}"