CREATE TABLE acoes_b3(
   id SERIAL PRIMARY KEY,
    ticker VARCHAR(10) NOT NULL,
    nome_empresa VARCHAR(100) NOT NULL,
    setor VARCHAR(50),
    preco DECIMAL(10, 2),
    data_cotacao DATE NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

select * from acoes_b3;
