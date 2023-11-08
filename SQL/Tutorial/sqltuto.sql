CREATE DATABASE Elefante -- Cria um Database

CREATE TABLE Pessoa(codPessoa INT NOT NULL IDENTITY(1,1), --Se da o valor do ID automaticamente
cpf INT NOT NULL, --Cria um elemento Inteiro
Nome VARCHAR(20) NOT NULL, --Cria um elemnto String
);

INSERT INTO Pessoa VALUES -- Adciona os elementos
(20,'Jao');


SELECT *FROM Pessoa -- Mostra os elementos

DROP TABLE Pessoa --Deletar