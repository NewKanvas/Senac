CREATE DATABASE floricultura;

-- Criação das TABLES

USE floricultura;
CREATE TABLE `cliente` (
  `codcliente` INT(11) NOT NULL PRIMARY KEY auto_increment,
  `rg` VARCHAR(20) NOT NULL,
  `nome` VARCHAR(20) NOT NULL,
  `telefone` VARCHAR(14) NOT NULL,
  `endereco` VARCHAR(30) NOT NULL
);

CREATE TABLE `produto` (
  `codproduto` INT(11) NOT NULL PRIMARY KEY auto_increment,
  `nome` VARCHAR(20) NOT NULL,
  `tipo` VARCHAR(20) NOT NULL,
  `preco` FLOAT NOT NULL,
  `quantidade` INT(11) NOT NULL
  );
  
CREATE TABLE `pedido` (
	`codpedido` INT(11) NOT NULL PRIMARY KEY auto_increment,
    `codcliente` INT(11) NOT NULL,
    `data` DATE NOT NULL,
    `vtotal` FLOAT NOT NULL,
    `codproduto` INT(11) NOT NULL
);

ALTER TABLE pedido ADD CONSTRAINT fk_cliente
FOREIGN KEY(codcliente) 
REFERENCES cliente(codcliente);

ALTER TABLE pedido ADD CONSTRAINT fk_produto
FOREIGN KEY(codproduto) 
REFERENCES produto(codproduto);

-- Inserindo

INSERT INTO cliente(codcliente,rg,nome,telefone,endereco)
 VALUES 
	(NULL, '2323232323', 'Jonas', '2199999999', 'Rua 12'),
	(NULL, '1414141414', 'Maria', '3399999999', 'Rua 66');
 
INSERT INTO produto(codproduto,nome,tipo,preco,quantidade)
VALUES
	(NULL,'vaso1','vaso',10.99,12),
    (NULL,'vaso2','vaso',15.50,20),
    (NULL,'semente1','semente',5.99,40);

INSERT INTO pedido(codpedido,codcliente,data,vtotal,codproduto)
VALUES
	(NULL,'1','2023/11/09',100,3),
    (NULL,'1','2023/11/09',100,2);


