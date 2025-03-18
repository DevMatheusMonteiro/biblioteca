from util import ler_csv, inserir_dados, renomear_coluna, consultar_dados, escrever_json

df_autores = ler_csv("autores")
df_autores = renomear_coluna(df_autores,{"pais_origem": "pais", "id_autor": "id"})
df_livros = ler_csv("livros")
df_livros = renomear_coluna(df_livros,{"ISBN": "isbn", "disponibilidade": "estoque", "id_livro": "id"})
df_usuarios = ler_csv("usuarios")
df_usuarios = renomear_coluna(df_usuarios, {"id_usuario": "id"})
df_usuarios["nome_completo"] = df_usuarios["nome"] + " " + df_usuarios["sobrenome"]
df_usuarios = df_usuarios.drop(columns=["nome", "sobrenome"])
df_emprestimos = ler_csv("emprestimos")
df_emprestimos = renomear_coluna(df_emprestimos,{"id_livro": "livro_id", "id_usuario": "usuario_id"})
df_livros_autores = ler_csv("livros_autores")
df_livros_autores = renomear_coluna(df_livros_autores,{"id_livro": "livro_id", "id_autor": "autor_id"})

# Inserindo os dados
""" 
inserir_dados(df_autores, "autor")
inserir_dados(df_livros, "livro")
inserir_dados(df_livros_autores, "livro_autor")
inserir_dados(df_usuarios, "usuario")
inserir_dados(df_emprestimos, "emprestimo") 
"""
autores_piquenique = consultar_dados("""
SELECT a.id, a.nome, a.pais FROM autor a 
INNER JOIN livro_autor la ON a.id = la.autor_id 
INNER JOIN livro l ON l.id = la.livro_id
WHERE l.titulo = 'Piquenique na Estrada';
""")

livros_philip = consultar_dados("""
SELECT 
l.id, 
l.titulo,
l.isbn,
l.genero,
l.data_publicacao,
l.qtd_paginas,
l.estoque
FROM livro l 
INNER JOIN livro_autor la ON l.id = la.livro_id
INNER JOIN autor a ON a.id = la.autor_id
WHERE a.nome = 'Philip K. Dick';
""")

livros_emprestimo = consultar_dados("""
SELECT
e.data_emprestimo,
e.data_devolucao,
l.id as livro_id, 
l.titulo as livro_alugado,
l.isbn as livro_isbn,
l.genero as livro_genero,
l.data_publicacao as livro_data_publicacao,
l.qtd_paginas as livro_qtd_paginas,
l.estoque as livro_estoque
FROM usuario u
INNER JOIN emprestimo e ON u.id = e.usuario_id
INNER JOIN livro l ON l.id = e.livro_id
WHERE u.nome_completo = 'Pedro Vinicius' AND e.data_devolucao IS NULL;
""")

escrever_json(autores_piquenique, "autores")
escrever_json(livros_philip, "livros")
escrever_json(livros_emprestimo, "emprestimos")