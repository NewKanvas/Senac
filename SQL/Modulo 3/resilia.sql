CREATE DATABASE resilia;

USE resilia;

CREATE TABLE facilitadores(
	id_facilitadores INT NOT NULL PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    cpf VARCHAR(14) NOT NULL,
    frente CHAR(4) NOT NULL
);

CREATE TABLE resilientes(
	id_resilientes INT NOT NULL PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    cpf VARCHAR(14) NOT NULL,
    turma CHAR(11) NOT NULL
);

use resilia;
LOAD DATA INFILE '\facilitadores.csv'
INTO TABLE facilitadores
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

use resilia;
LOAD DATA INFILE '\aluno.csv'
INTO TABLE resilientes
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

SELECT * FROM facilitadores;
SELECT * FROM resilientes;

update facilitadores set frente='Teste' 
where id_facilitadores=1;
select * from facilitadores;

