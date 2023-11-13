create database magazu;

-- Criar Tabelas

-- Estrutura da tabela `cliente`

use magazu;
CREATE TABLE `cliente` (
  `codcliente` int(11) NOT NULL PRIMARY KEY auto_increment,
  `nome` varchar(20) NOT NULL,
  `endereco` varchar(30) NOT NULL,
  `celular` varchar(14) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;



-- Estrutura da tabela `fornecedor`

CREATE TABLE `fornecedor` (
  `codfornecedor` int(11) NOT NULL PRIMARY KEY auto_increment,
  `razaosocial` varchar(40) NOT NULL,
  `cnpj` varchar(18) NOT NULL,
  `endereco` varchar(40) NOT NULL,
  `email` varchar(40) NOT NULL,
  `telefone` varchar(14) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;


-- Estrutura da tabela `pedido`


CREATE TABLE `pedido` (
  `codpedido` int(11) NOT NULL PRIMARY KEY AUTO_INCREMENT,
  `datapedido` date NOT NULL,
  `quantidade` int(11) NOT NULL,
  `valor` float NOT NULL,
  `total` float NOT NULL,
  `codcliente` int(11) NOT NULL,
  `codproduto` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- Estrutura da tabela `produto`

CREATE TABLE `produto` (
  `codproduto` int(11) NOT NULL PRIMARY KEY AUTO_INCREMENT, 
  `descricao` varchar(40) NOT NULL,
  `categoria` varchar(25) NOT NULL,
  `preco` float NOT NULL,
  `data` date NOT NULL,
  `codfornecedor` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;


-- Comandos:

SELECT *FROM X -- Mostra os elementos

DROP TABLE X --Deletar

ALTER TABLE `X`
  ADD PRIMARY KEY (`X1`); -- Adciona um Key primaria
  ADD KEY (`XX`); -- Adciona uma Key


-- Estrutura para adcionar a key extrangeira

alter table produto add constraint fk_fornecedor
-- ALTER TABLE pedido (adicionando uma restrição (constraint) a essa tabela.)
-- ADD CONSTRAINT fk_produtos (nova restrição que será adicionada à tabela como "fk_produtos")
foreign key(codfornecedor) 
-- Indica que a restrição que está sendo adicionada é uma chave estrangeira
-- Isso significa que a coluna "codfornecedor" na tabela "pedido" será uma chave estrangeira. Uma chave estrangeira é
-- uma coluna que estabelece uma relação entre duas tabelas, permitindo que os dados em uma tabela façam referência aos dados em outra tabela.
references fornecedor(codfornecedor)
-- Aqui, você especifica a tabela e a coluna que a chave estrangeira "codfornecedor" na tabela "produto" faz referência. 

alter table pedido add constraint fk_produtos
foreign key(codproduto) 
references produto(codproduto);

alter table pedido add constraint fk_cliente 
foreign key(codcliente) 
references cliente(codcliente);



-- Inserts

-- Cliente

INSERT INTO cliente(codcliente,nome,endereco,celular)
 VALUES 
 (NULL, 'Ana', 'Rua abc', '245545454'),
(NULL, 'Ana', 'Rua abc', '245545454') ;

-- Fornecedor

INSERT INTO fornecedor(codfornecedor,razaosocial,cnpj, 
endereco,email,telefone) 
VALUES (null, 'Empresa abc', 'Abc Equipamentos', '296767767676', 'a@gmail.com', '32332');

-- Produto

INSERT INTO produto(codproduto,descricao,categoria, 
preco, data,codfornecedor) VALUES (1,'Notebook','Info',3000.00,'02/02/2022',1)

-- Pedido

INSERT INTO pedido(codpedido,datapedido, quantidade, valor, total,
 codcliente, codproduto) VALUES (NULL, '2023-11-06', '10', '250', '2500', '1', '1');


 -- Criando Novas Tables
 
use magazu;

CREATE TABLE departamento (
  coddepartamento int(11) NOT NULL primary key 
  AUTO_INCREMENT,
  nome varchar(20) NOT NULL,
  sigla varchar(30) NOT NULL,
  valorOrcamento float NOT NULL
)


CREATE TABLE funcionario(
  codfuncionario int(11) NOT NULL primary key 
  AUTO_INCREMENT,
  nome varchar(20) NOT NULL,
  cargo varchar(30) NOT NULL,
  salario float NOT NULL,
  coddepartamento int not null
) ;

ALTER TABLE funcionario ADD CONSTRAINT fk_funcionario
foreign key(coddepartamento)
references departamento(coddepartamento);




CREATE TABLE itempedido(
  numeroitem int(11) NOT NULL primary key 
  AUTO_INCREMENT,
  qtd int NOT NULL,
  valor float NOT NULL,
  codpedido int not null
) ;


ALTER TABLE itempedido ADD CONSTRAINT fk_codpedido
FOREIGN KEY(codpedido)
REFERENCES pedido(codpedido)