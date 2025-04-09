from database_config_sqlalchemy import sql, Base

livro_autor = sql.Table(
    "livro_autor", Base.metadata,
    sql.Column("livro_id", sql.Integer, sql.ForeignKey("livro.id"), primary_key=True),
    sql.Column("autor_id", sql.Integer, sql.ForeignKey("autor.id"), primary_key=True)
)