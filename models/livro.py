from database_config_sqlalchemy import Base, sql, orm
from .livro_autor import livro_autor

class Livro(Base):
    __tablename__ = "livro"
    
    id = sql.Column(sql.Integer, primary_key=True, autoincrement=True)
    titulo = sql.Column(sql.String, nullable=False)
    isbn = sql.Column(sql.String, nullable=False)
    genero = sql.Column(sql.String, nullable=False)
    data_publicacao = sql.Column(sql.String, nullable=False)
    qtd_paginas = sql.Column(sql.Integer, nullable=False)
    estoque = sql.Column(sql.Integer, nullable=False)

    autores = orm.relationship("Autor", secondary=livro_autor, back_populates="livros")
    emprestimos = orm.relationship("Emprestimo", back_populates="livro")

    def __str__(self):
        return f"ID - {self.id} | Título - {self.titulo} | ISBN - {self.genero} | Data de Publicação - {self.data_publicacao} | Quantidade de Páginas - {self.qtd_paginas} | Estoque - {self.estoque}"