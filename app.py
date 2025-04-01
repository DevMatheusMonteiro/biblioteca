from util import inserir_dados
from web_scraping import parser_html
import pandas as pd

(livros, autores, livro_autor) = parser_html()

df_livros = pd.DataFrame(livros)
df_autores = pd.DataFrame(autores)
df_livro_autor = pd.DataFrame(livro_autor)

inserir_dados(df_autores, "autor")
inserir_dados(df_livros, "livro")
inserir_dados(df_livro_autor, "livro_autor")