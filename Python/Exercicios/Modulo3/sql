create database magazu;

use magazu;
create table cliente(codCliente int Not Null auto_increment PRIMARY KEY,
nome varchar(20) Not Null,
endereco varchar(30) Not Null,
tel varchar(14) Not Null);

use magazu;
create table produto(codproduto int Not Null auto_increment PRIMARY KEY,
descricao varchar(40) Not Null,
categoria varchar(30) Not Null,
preco float not null,
data date not null);


use magazu;
create table fornercedor(codfonercedor int Not Null auto_increment PRIMARY KEY,
razaosocial varchar(40) not null,
cnpj varchar(18) not null,
endereco varchar(40) not null);


use magazu;
create table pedido(codpedido int Not Null auto_increment PRIMARY KEY,
datapedido date not null,
quantidade int not null,
valor float not null,
total float not null,
codcliente int not null,
codproduto int not null
);

show tables;
select* from produto;
