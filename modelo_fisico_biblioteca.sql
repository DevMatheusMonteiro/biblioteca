CREATE TABLE IF NOT EXISTS autor (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome VARCHAR(255) NOT NULL,  
    pais VARCHAR(255) NOT NULL
);
CREATE TABLE IF NOT EXISTS livro (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    titulo VARCHAR(255) NOT NULL,
    isbn VARCHAR(13) NOT NULL UNIQUE,
    genero VARCHAR(50) NOT NULL,
    data_publicacao DATETIME NOT NULL,
    qtd_paginas INTEGER NOT NULL,
    estoque INTEGER NOT NULL DEFAULT 0
);
CREATE TABLE IF NOT EXISTS livro_Autor (
    livro_id INTEGER NOT NULL,
    autor_id INTEGER NOT NULL,
    PRIMARY KEY (livro_id, autor_id),
    FOREIGN KEY (livro_id) REFERENCES livro(id),
    FOREIGN KEY (autor_id) REFERENCES autor(id)
);
CREATE TABLE IF NOT EXISTS usuario (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome_completo VARCHAR(255) NOT NULL,
    data_nascimento DATETIME NOT NULL
);
CREATE TABLE IF NOT EXISTS emprestimo (
    data_emprestimo DATETIME NOT NULL,
    data_devolucao DATETIME,
    usuario_id INTEGER,
    livro_id INTEGER,
    PRIMARY KEY (livro_id, usuario_id),
    FOREIGN KEY (usuario_id) REFERENCES usuario(id),
    FOREIGN KEY (livro_id) REFERENCES livro(id),
    CHECK (data_devolucao IS NULL OR data_devolucao > data_emprestimo)
);