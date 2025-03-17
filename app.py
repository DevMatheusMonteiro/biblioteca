from util import ler_csv, inserir_dados, renomear_coluna

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

inserir_dados(df_autores, "autor")
inserir_dados(df_livros, "livro")
inserir_dados(df_livros_autores, "livro_autor")
inserir_dados(df_usuarios, "usuario")
inserir_dados(df_emprestimos, "emprestimo")