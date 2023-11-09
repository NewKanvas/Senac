CREATE DATABASE spotify;

-- Criando Tabelas

USE spotify;
CREATE TABLE `artista` (
	`codartista` INT(11) NOT NULL PRIMARY KEY auto_increment,
	`nome` VARCHAR(20) NOT NULL
);


CREATE TABLE `musica` (
	`codmusica` INT(11) NOT NULL PRIMARY KEY auto_increment,
	`nome` VARCHAR(20) NOT NULL,
	`categoria` varchar(50) NOT NULL,
	`duracao` time NOT NULL,
    `codartista` INT(11)
);

CREATE TABLE `usuario` (
	`codusario` INT(11) NOT NULL PRIMARY KEY auto_increment,
	`nome` VARCHAR(20) NOT NULL,
    `email` VARCHAR(20) NOT NULL,
    `senha` VARCHAR(20) NOT NULL
);


CREATE TABLE `registros`(
	`codmusica` INT(11) NOT NULL,
    `codusario` INT(11) NOT NULL,
    `data` DATE NOT NULL
);

-- Inserir

INSERT INTO artista(codartista,nome)
 VALUES 
	(NULL,'Juan Santano'),
    (NULL,'Marciana Grunge'),
    (NULL,'Popi');
    
INSERT INTO musica(codmusica,nome,categoria,duracao,codartista)
 VALUES 
	(NULL,'Juan Santano'),
    (NULL,'Marciana Grunge'),
    (NULL,'Popi');