CREATE DATABASE RESILIADATA;
USE RESILIADATA;

CREATE TABLE empresa 
( 
    id_empresa INT PRIMARY KEY AUTO_INCREMENT,  
    nome_empresa VARCHAR(255) NOT NULL,  
    endereco VARCHAR(255) NOT NULL,  
    telefone VARCHAR(255) NOT NULL
); 

CREATE TABLE tecnologias
( 
    id_tecnologias INT PRIMARY KEY AUTO_INCREMENT,  
    area VARCHAR(255) NOT NULL,  
    nome_tecnologia VARCHAR(255) NOT NULL
); 

CREATE TABLE tecnologia_empresa 
( 
    id_empresa INT NOT NULL,  
    id_tecnologias INT NOT NULL,  
    nivel_utilizacao INT NOT NULL  -- 1 a 5 (Sendo 1 pouco usado e 5 muito usado)
); 

CREATE TABLE colaborador
( 
    id_colaborador INT PRIMARY KEY AUTO_INCREMENT,  
    nome VARCHAR(255) NOT NULL,  
    cargo VARCHAR(255) NOT NULL,  
    id_empresa INT NOT NULL 
); 

ALTER TABLE tecnologia_empresa ADD FOREIGN KEY(id_empresa) REFERENCES empresa (id_empresa);
ALTER TABLE tecnologia_empresa ADD FOREIGN KEY(id_tecnologias) REFERENCES tecnologias (id_tecnologias);
ALTER TABLE colaborador ADD FOREIGN KEY(id_empresa) REFERENCES empresa (id_empresa);


-- Inserir dados na tabela empresa
INSERT INTO empresa(nome_empresa, endereco, telefone) 
VALUES 
('PinkMello', '123 Main Street', '555-1234'),
('WebZoom', '456 Oak Avenue', '555-5678');

-- Inserir dados na tabela tecnologias
INSERT INTO tecnologias(area, nome_tecnologia) 
VALUES 
('Web Development', 'HTML/CSS'),
('Data Science', 'Python');

-- Inserir dados na tabela colaborador
INSERT INTO colaborador(nome, cargo, id_empresa) 
VALUES 
('John Doe', 'Developer', 1),
('Jane Smith', 'Data Scientist', 2);

-- Inserir dados na tabela tecnologia_empresa
INSERT INTO tecnologia_empresa(id_empresa, id_tecnologias, nivel_utilizacao) 
VALUES 
(1, 1, 4),
(1, 2, 3),
(2, 1, 5),
(2, 2, 2);
