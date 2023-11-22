create database pizzaria;

drop database pizzaria;

use pizzaria;
CREATE TABLE tb_cliente(
	`id_cliente` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `nome` VARCHAR(30) NOT NULL,
    `email` VARCHAR(30) NOT NULL,
    `enderececo` VARCHAR(30) NOT NULL
);

ALTER TABLE tb_cliente
CHANGE COLUMN enderececo endereco VARCHAR(30) NOT NULL;


CREATE TABLE tb_pedido(
	`id_pedido` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `id_cliente` INT NOT NULL,
    `observacao` VARCHAR(30) NOT NULL,
    `tipo_entrega` VARCHAR(30) NOT NULL,
    `preco` FLOAT NOT NULL,
    `data_pedido` DATE NOT NULL
);

CREATE TABLE tb_pizza(
	`id_pizza` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `nome` VARCHAR(30) NOT NULL,
    `descricao` VARCHAR(100) NOT NULL,
    `categoria` VARCHAR(30) NOT NULL,
    `preco` FLOAT NOT NULL
);

CREATE TABLE tb_pedido_pizza(
	`id_pedido` INT NOT NULL,
    `id_pizza` INT NOT NULL,
    `quantidade` VARCHAR(30) NOT NULL
);

ALTER TABLE tb_pedido ADD FOREIGN KEY(id_cliente) REFERENCES tb_cliente (id_cliente);
ALTER TABLE tb_pedido_pizza ADD FOREIGN KEY(id_pedido) REFERENCES tb_pedido (id_pedido);
ALTER TABLE tb_pedido_pizza ADD FOREIGN KEY(id_pizza) REFERENCES tb_pizza (id_pizza);

SELECT * FROM tb_pizza;
SELECT * FROM tb_cliente;
SELECT * FROM tb_pedido;
SELECT * FROM tb_pedido_pizza;

DELETE FROM tb_pizza WHERE id_pizza = 3; 

INSERT INTO tb_pizza(nome,descricao,categoria,preco) 
VALUES ('pepperoni','Salame, linguiça diferente','pizza',20.99),
('4queijo','Queijos desconhecidos','pizza',10.99),
('romeuejulieta','"Ela tomou do mesmo veneno que eu"','pizza',54.99);

INSERT INTO tb_cliente(nome,email,endereco) 
VALUES ('Jonas','j@mail','Rua 69'),
('Maria','m@mail','Rua 88'),
('Romeu','r@mail','Rua 0');

INSERT INTO tb_cliente (nome, email, endereco)
VALUES
('Carlos', 'carlos@gmail.com', 'Avenida Central n789'),
('Fernanda', 'fernanda@gmail.com', 'Rua das Flores n456'),
('Lucia', 'lucia@gmail.com', 'Travessa da Paz n222'),
('Roberto', 'roberto@gmail.com', 'Alameda dos Sonhos n333'),
('Juliana', 'juliana@gmail.com', 'Praça da Liberdade n777'),
('Mateus', 'mateus@gmail.com', 'Rua da Amizade n888'),
('Isabel', 'isabel@gmail.com', 'Avenida do Sol n555');


INSERT INTO tb_pedido (id_cliente, observacao, tipo_entrega, preco, data_pedido)
VALUES
(1, 'Pedido 1', 'Entrega expressa', 25.50, '2023-11-22'),
(2, 'Pedido 2', 'Entrega padrão', 30.00, '2023-11-23'),
(3, 'Pedido 3', 'Retirada na loja', 20.75, '2023-11-24'),
(4, 'Pedido 4', 'Entrega expressa', 40.20, '2023-11-25'),
(5, 'Pedido 5', 'Entrega expressa', 35.90, '2023-12-02'),
(6, 'Pedido 6', 'Retirada na loja', 18.50, '2023-12-03'),
(7, 'Pedido 7', 'Entrega padrão', 22.75, '2023-12-04'),
(8, 'Pedido 8', 'Entrega expressa', 27.30, '2023-12-05'),
(9, 'Pedido 9', 'Retirada na loja', 33.40, '2023-12-06');

INSERT INTO tb_pedido_pizza(id_pedido,id_pizza,quantidade) 
VALUES (4,4,'Meia'),
(5,4,'Inteira'),
(6,5,'Inteira'),
(7,5,'Meia'),
(8,6,'Inteira'),
(9,6,'Inteira');


SELECT nome AS Teste from tb_cliente;

SELECT nome,endereco from tb_cliente order by nome;

SELECT preco,tipo_entrega FROM tb_pedido WHERE preco >=10;

-- <> Diferente
SELECT preco,tipo_entrega FROM tb_pedido WHERE preco <> 25.5;

SELECT preco, tipo_entrega
FROM tb_pedido 
WHERE preco <> 35 AND tipo_entrega = 'Retirada na loja';
