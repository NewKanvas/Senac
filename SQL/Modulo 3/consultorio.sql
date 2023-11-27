CREATE DATABASE consultorio;
USE consultorio;

CREATE TABLE paciente(
	id_paciente INT NOT NULL PRIMARY KEY,
    nome VARCHAR(30) NOT NULL
);

CREATE TABLE medico(
	id_medico INT NOT NULL PRIMARY KEY,
    nome VARCHAR(30) NOT NULL,
    crm VARCHAR(30) NOT NULL,
    especialiazacao VARCHAR(30) NOT NULL
);

CREATE TABLE consulta(
	id_consulta INT NOT NULL PRIMARY KEY,
    id_paciente INT NOT NULL,
    id_medico INT NOT NULL
);

ALTER TABLE consulta ADD FOREIGN KEY(id_paciente) REFERENCES paciente (id_paciente);
ALTER TABLE consulta ADD FOREIGN KEY(id_medico) REFERENCES medico (id_medico);

