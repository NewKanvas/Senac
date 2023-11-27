
DROP DATABASE pizzaria;

create database pizzaria;
use pizzaria;

CREATE TABLE tb_cliente( id_cliente INT NOT NULL PRIMARY KEY AUTO_INCREMENT, nome VARCHAR(30) NOT NULL, email VARCHAR(30) NOT NULL, endereco VARCHAR(90) NOT NULL );

CREATE TABLE tb_pedido( id_pedido INT NOT NULL PRIMARY KEY AUTO_INCREMENT, id_cliente INT NOT NULL, observacao VARCHAR(30) NOT NULL, tipo_entrega VARCHAR(30) NOT NULL, preco FLOAT NOT NULL, data_pedido DATE NOT NULL );

CREATE TABLE tb_pizza( id_pizza INT NOT NULL PRIMARY KEY AUTO_INCREMENT, nome VARCHAR(30) NOT NULL, descricao VARCHAR(100) NOT NULL, categoria VARCHAR(30) NOT NULL, preco FLOAT NOT NULL );

CREATE TABLE tb_pedido_pizza( id_pedido INT NOT NULL, id_pizza INT NOT NULL, quantidade VARCHAR(30) NOT NULL );

-- INSERINDO AS CHAVES ESTRANGEIRAS
ALTER TABLE tb_pedido ADD FOREIGN KEY(id_cliente) REFERENCES tb_cliente (id_cliente); ALTER TABLE tb_pedido_pizza ADD FOREIGN KEY(id_pedido) REFERENCES tb_pedido (id_pedido); ALTER TABLE tb_pedido_pizza ADD FOREIGN KEY(id_pizza) REFERENCES tb_pizza (id_pizza);

-- INSERINDO CLIENTES
INSERT INTO tb_cliente (nome, email, endereco) VALUES ('Antonio', 'antonio@gmail.com', 'Rua prof Olinto n393'), ('Nunes', 'nunes@gmail.com', 'Rua prof de oliveira n111'), ('alules', 'alules@gmail.com', 'Estrada porto nac n373');

INSERT INTO tb_cliente (nome, email, endereco) VALUES ('Carlos', 'carlos@gmail.com', 'Avenida Central n789'), ('Fernanda', 'fernanda@gmail.com', 'Rua das Flores n456'), ('Lucia', 'lucia@gmail.com', 'Travessa da Paz n222'), ('Roberto', 'roberto@gmail.com', 'Alameda dos Sonhos n333'), ('Juliana', 'juliana@gmail.com', 'Praça da Liberdade n777'), ('Mateus', 'mateus@gmail.com', 'Rua da Amizade n888'), ('Isabel', 'isabel@gmail.com', 'Avenida do Sol n555');

-- INSERINDO AS PIZZAS DISPONIVEIS
INSERT INTO tb_pizza(nome, descricao, categoria, preco) VALUES('pepperoni', 'de linguica', 'Contém Lactose', 35.00), ('Frango com Catupiry', 'Frango, catupiry, queijo, molho', 'Contém Lactose', 38.00), ('4 Queijos', 'Mussarela, Minas, gorgonzola, buffala, molho', 'Contém Lactose', 38.00);

-- NOVAS PIZZAS ZERO LACTOSE
INSERT INTO tb_pizza(nome, descricao, categoria, preco) VALUES('Vegetariana', 'Tomate, cogumelos, cebola, pimentão e azeitonas.','Zero Lactose',50), ('Margarita sem Queijo', 'Molho de tomate, tomate fatiado, manjericão e azeite de oliva.', 'Zero Lactose', 48), ('Mediterrânea','Molho de tomate, espinafre, tomate seco, azeitonas e alho.','Zero Lactese',43), ('Primavera', 'Molho de tomate, abobrinha, tomate cereja, brócolis e manjericão.', 'Zero Lactose', 45);

-- INSERINDO PEDIDOS
INSERT INTO tb_pedido (id_cliente, observacao, tipo_entrega, preco, data_pedido) VALUES (1, 'Pedido 1', 'Entrega expressa', 35, '2023-11-22'), (2, 'Pedido 2', 'Entrega padrão', 38, '2023-11-23'), (3, 'Pedido 3', 'Retirada na loja', 38, '2023-11-24'), (4, 'Pedido 4', 'Entrega expressa', 35, '2023-11-25'), (5, 'Pedido 5', 'Entrega expressa', 38, '2023-12-02'), (6, 'Pedido 6', 'Retirada na loja', 38, '2023-12-03'), (7, 'Pedido 7', 'Entrega padrão', 38, '2023-12-04'), (8, 'Pedido 8', 'Entrega expressa', 35, '2023-12-05'), (9, 'Pedido 9', 'Retirada na loja', 38, '2023-12-06');

-- INSERINDO NOVOS PEDIDOS
INSERT INTO tb_pedido (id_cliente, observacao, tipo_entrega, preco, data_pedido) VALUES (1, 'Pedido 10', 'Entrega expressa', 111, '21-04-2021'), (5, 'Pedido 11', 'Entrega expressa', 108, '25-04-2021'), (4, 'Pedido 12', 'Entrega expressa', 138, '23-04-2021');

-- INSERINDO PEDIDO_PIZZA
INSERT INTO tb_pedido_pizza (id_pedido, id_pizza, quantidade) VALUES (1, 1, 'MEIA'), (2, 2, 'INTEIRA'), (3, 3, 'MEIA'), (4, 1, 'MEIA'), (5, 3, 'INTEIRA'), (6, 2, 'MEIA'), (7, 3, 'INTEIRA'), (8, 1, 'INTEIRA'), (9, 2, 'INTEIRA');

-- INSERINDO NOVOS PEDIDO_PIZZA
INSERT INTO tb_pedido_pizza (id_pedido, id_pizza, quantidade) VALUES (10, 1, 'MEIA'), (11, 2, 'INTEIRA'), (12, 3, 'MEIA');

SELECT *
FROM tb_pedido_pizza;

DELETE FROM tb_pedido
WHERE observacao LIKE 'P%';

-- MUDANDO O NOME DE UMA COLUNA
ALTER TABLE tb_cliente CHANGE COLUMN enderececo endereco VARCHAR(255);

ALTER TABLE tb_pizza CHANGE ROW

-- SELECIONANDO UMA TABELA
SELECT * FROM tb_pedido WHERE id_pedido = 0;

-- SELECIONANDO A COLUNA pedido_pizza
SELECT * FROM tb_pedido_pizza; SELECT * FROM tb_pizza;

-- DELETANDO ITENS DE UMA TABELA
DELETE FROM tb_pedido WHERE id_pedido BETWEEN 0 AND 27;

-- DELETANDO TODOS OS ITENS DE UMA TABELA
DROP FROM tb_pedido;

-- SELECIONANDO NOME E ENDEREÇO, ORDENANDO POR ORDEM ALFABÉTICA
SELECT nome, endereco FROM tb_cliente ORDER BY nome;

-- CONSULTANDO O PRECO E O TIPO DA ENTREGA COM O OPERADOR >=
SELECT preco,tipo_entrega FROM tb_pedido WHERE preco >=10;

SELECT preco, tipo_entrega FROM tb_pedido WHERE preco <> 35 AND tipo_entrega='Retirada na loja';

SELECT * FROM tb_cliente WHERE nome LIKE 'a%';

SELECT * FROM tb_cliente WHERE email LIKE '%hotmail.com';

SELECT * FROM tb_pizza WHERE categoria = 'Zero Lactose';

SELECT * FROM tb_pizza WHERE categoria <> 'Zero Lactose';

UPDATE tb_pizza SET categoria = 'Zero Lactese' WHERE categoria = 'Zero Lactose';

UPDATE tb_pizza SET categoria = 'Zero Lactose' WHERE categoria = 'Zero Lactese' LIMIT 4;

SELECT * FROM tb_cliente;

ALTER TABLE tb_cliente
CHANGE COLUMN enderececo endereco VARCHAR(255);