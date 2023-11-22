CREATE DATABASE Elefante -- Cria um Database

CREATE TABLE Pessoa(codPessoa INT NOT NULL IDENTITY(1,1), --Se da o valor do ID automaticamente
cpf VARCHAR NOT NULL, --Cria um elemnto String
Nome VARCHAR(20) NOT NULL, --Cria um elemnto String (Limite 20 Caracteres)
Idade INT NOT NULL, --Cria um elemento Inteiro (Limite 11)
);

INSERT INTO Pessoa VALUES -- Adciona os elementos
(20,'Jao');

INSERT INTO tb_pizza(nome,descricao,categoria,preco) 
VALUES ('pepperoni','pizza','pizza',20.99),
('4queijo','pizza','pizza',10.99),
('romeuejulieta','pizza','pizza',54.99);

SELECT * FROM Pessoa -- Mostra os elementos

SELECT nome AS Teste from tb_cliente;

SELECT nome,endereco from tb_cliente order by nome;

-- >= Maior ou igual
SELECT preco,tipo_entrega FROM tb_pedido WHERE preco >=10;

-- <> Diferente
SELECT preco,tipo_entrega FROM tb_pedido WHERE preco <> 25.5;

SELECT preco, tipo_entrega
FROM tb_pedido 
WHERE preco <> 35 AND tipo_entrega = 'Retirada na loja';

-- Pegar com a primeira letra J
SELECT * FROM Pessoa WHERE Nome LIKE 'j%';

-- Pegar com a ultima letra J
SELECT * FROM Pessoa WHERE Nome LIKE '%j';

DROP TABLE Pessoa --Deletar

TRUNCATE TABLE Pessoa -- Deleta todos os valores da tabela

DELETE FROM Pessoa WHERE Nome ='Jao'

ALTER TABLE Pessoa 
CHANGE COLUMN Nome nome VARCHAR(20) NOT NULL


UPDATE tb_pizza
SET categoria = 'Zero Lactese'
WHERE categoria = 'Zero Lactose';

UPDATE tb_pizza
SET categoria = 'Zero Lactose'
WHERE categoria = 'Zero Lactese'
LIMIT 4;

SELECT *
FROM tb_pizza;