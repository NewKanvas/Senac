CREATE  DATABASE blocc;
USE blocc;

DROP DATABASE blocc;

CREATE TABLE A(
	`id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `letter` VARCHAR(30) NOT NULL,
    `form` VARCHAR(30) NOT NULL,
    `color` VARCHAR(30) NOT NULL,
    `fruit` VARCHAR(30) NOT NULL,
    `number` INT NOT NULL
);

CREATE TABLE B(
	`id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `letra` VARCHAR(30) NOT NULL,
    `forma` VARCHAR(30) NOT NULL,
    `cor` VARCHAR(30) NOT NULL,
    `fruta` VARCHAR(30) NOT NULL,
    `numero` INT NOT NULL
);

-- ############################################################

-- Inserir dados na tabela A
INSERT INTO A (letter, form, color, fruit, number) VALUES
('A1', 'Square', 'Red', 'Apple', 1),
('A2', 'Circle', 'Yellow', 'Banana', 2),
('A3', 'Triangle', 'Green', 'Grapes', 3),
('A4', 'Rectangle', 'Blue', 'Blueberry', 4),
('A5', 'Hexagon', 'Purple', 'Plum', 5),
('A6', 'Oval', 'Orange', 'Orange', 6),
('A7', 'Star', 'Pink', 'Strawberry', 7),
('A8', 'Diamond', 'Brown', 'Date', 8),
('A9', 'Heart', 'Black', 'Blackberry', 9),
('A10', 'Pentagon', 'White', 'Coconut', 10);

-- Inserir dados na tabela B 
INSERT INTO B (letra, forma, cor, fruta, numero) VALUES
('B1', 'Quadrado', 'Vermelho', 'Maçã', 1),
('B2', 'Círculo', 'Amarelo', 'Banana', 2),
('B3', 'Triângulo', 'Verde', 'Uvas', 3),
('B4', 'Retângulo', 'Azul', 'Mirtilo', 4),
('B5', 'Hexágono', 'Roxo', 'Ameixa', 5),
('B6', 'Oval', 'Laranja', 'Laranja', 6),
('B7', 'Estrela', 'Rosa', 'Morango', 7),
('B8', 'Diamante', 'Marrom', 'Tâmara', 8),
('B9', 'Coração', 'Preto', 'Amora', 9),
('B10', 'Pentágono', 'Branco', 'Coco', 10);

-- ############################################################

SELECT * FROM A;
SELECT * FROM B;

SELECT * FROM A
JOIN B on A.id = B.id;

SELECT * FROM A
INNER JOIN B on A.id = B.id;

select CONCAT(nome,email) from tb_cliente;
select UPPER(nome) from tb_cliente;
select LOWER(nome) from tb_cliente;

select UPPER(CONCAT(nome,email)) from tb_cliente;

select length(nome) from tb_cliente;
SELECT data_pedido from tb_pedido;
SELECT extract(year from data_pedido) from tb_pedido;
SELECT extract(month from data_pedido) from tb_pedido;