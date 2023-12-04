'''
O que é para fazer:

Crie uma tabela avançada chamada "funcionarios" com as seguintes colunas: "id" (inteiro), "nome" (texto), "idade" (inteiro), "salario" (decimal), "departamento" (texto) e "data_contratacao" (data).

Como Fazer:

    Abra o terminal do PostgreSQL e conecte-se ao banco de dados desejado;
    Utilize o comando ""CREATE TABLE"", seguido pelo nome da tabela que deseja criar;
    Crie as colunas usando o nome da coluna seguido do tipo de dado correspondente;
    Para a coluna ""id"", utilize o tipo de dado ""SERIAL PRIMARY KEY"" para que seja gerado automaticamente;
    Adicione as outras colunas com os tipos de dados corretos;
    Finalize a declaração da tabela com um ponto e vírgula.
'''

CREATE TABLE funcionarios(
    id SERIAL PRIMARY KEY,
    nome VARCHAR(30) NOT NULL,
    idade INT NOT NULL,
    salario FLOAT,
    departamento VARCHAR,
    data_contratacao DATA
);


SELECT c.nome,p.id FROM clientes c
INNER JOIN pedidos p ON p.id = c.id_cliente; 