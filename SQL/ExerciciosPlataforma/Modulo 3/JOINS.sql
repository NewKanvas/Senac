'''
1
O que é para fazer:

"Você precisa selecionar dados de duas tabelas diferentes no PostgreSQL usando o comando INNER JOIN. "

Como Fazer:

Supondo que temos duas tabelas ""clientes"" e ""pedidos"", e que cada pedido é vinculado a um único cliente através da coluna ""id_cliente"" na tabela ""pedidos"", enquanto a tabela ""clientes"" tem uma coluna ""id"" como chave primária;

    Abra o seu cliente PostgreSQL e conecte-se ao banco de dados desejado;
    Identifique as tabelas que deseja unir e suas respectivas chaves primárias;
    Utilize a sintaxe do INNER JOIN para unir as tabelas, especificando as chaves primárias de cada tabela a serem relacionadas;
    Especifique quais colunas de cada tabela você deseja selecionar no resultado da consulta;
    Execute a consulta e verifique os resultados.
'''

SELECT c.nome,p.id FROM clientes c
INNER JOIN pedidos p ON p.id = c.id_cliente; 


'''
2

O que é para fazer:

Você precisa selecionar dados de duas tabelas diferentes no PostgreSQL usando o comando INNER JOIN e aplicando uma condição de filtro na junção das tabelas.

Como Fazer:

Supondo que temos duas tabelas ""clientes"" e ""pedidos"", e que cada pedido é vinculado a um único cliente através da coluna ""id_cliente"" na tabela ""pedidos"", enquanto a tabela ""clientes"" tem uma coluna ""id"" como chave primária.

    Abra o seu cliente PostgreSQL e conecte-se ao banco de dados desejado.
    Identifique as tabelas que deseja unir e suas respectivas chaves primárias.
    Utilize a sintaxe do INNER JOIN para unir as tabelas, especificando as chaves primárias de cada tabela a serem relacionadas.
    Adicione a condição de filtro para a junção das tabelas usando a cláusula WHERE, especificando a coluna da tabela a ser filtrada e o valor desejado.
    Especifique quais colunas de cada tabela você deseja selecionar no resultado da consulta.
    Execute a consulta e verifique os resultados.
'''


'''
3

O que é para fazer:

Você precisa selecionar dados de três tabelas diferentes no PostgreSQL usando o comando INNER JOIN e agrupando os resultados por uma coluna específica.

Como Fazer:

Supondo que temos três tabelas ""clientes"", ""pedidos"" e ""itens_pedidos"", onde cada pedido possui vários itens, e cada item está vinculado a um único pedido e a um único produto através das colunas ""id_pedido"" e ""id_produto"", respectivamente.

    Abra o seu cliente PostgreSQL e conecte-se ao banco de dados desejado.
    Identifique as três tabelas que deseja unir e suas respectivas chaves primárias.
    Utilize a sintaxe do INNER JOIN para unir as tabelas, especificando as chaves primárias de cada tabela a serem relacionadas.
    Especifique quais colunas de cada tabela você deseja selecionar no resultado da consulta.
    Adicione a cláusula GROUP BY para agrupar os resultados por uma coluna específica.
    Execute a consulta e verifique os resultados.
'''



'''
4

O que é para fazer:

Você precisa selecionar dados de duas tabelas diferentes no PostgreSQL usando o comando INNER JOIN e ordenando os resultados por uma coluna específica.

Como Fazer:

Supondo que temos duas tabelas ""clientes"" e ""pedidos"", onde cada pedido é vinculado a um único cliente através da coluna ""id_cliente"" na tabela ""pedidos"", enquanto a tabela ""clientes"" tem uma coluna ""nome"" que indica o nome do cliente;

    Abra o seu cliente PostgreSQL e conecte-se ao banco de dados desejado;
    Identifique as tabelas que deseja unir e suas respectivas chaves primárias;
    Utilize a sintaxe do INNER JOIN para unir as tabelas, especificando as chaves primárias de cada tabela a ser relacionada;
    Especifique quais colunas de cada tabela você deseja selecionar no resultado da consulta;
    Adicione a cláusula ORDER BY para ordenar os resultados por uma coluna específica em ordem crescente ou decrescente;
    Execute a consulta e verifique os resultados.
'''


'''
5

O que é para fazer:

Você precisa selecionar dados de três tabelas diferentes no PostgreSQL usando o comando INNER JOIN e filtrando os resultados por uma condição específica.

Como Fazer:

Supondo que temos três tabelas ""clientes"", ""pedidos"" e ""itens_pedidos"", onde cada pedido possui vários itens, e cada item está vinculado a um único pedido e a um único produto através das colunas ""id_pedido"" e ""id_produto"", respectivamente;

    Abra o seu cliente PostgreSQL e conecte-se ao banco de dados desejado;
    Identifique as três tabelas que deseja unir e suas respectivas chaves primárias;
    Utilize a sintaxe do INNER JOIN para unir as tabelas, especificando as chaves primárias de cada tabela a ser relacionada;
    Especifique quais colunas de cada tabela você deseja selecionar no resultado da consulta;
    Adicione a cláusula WHERE para filtrar os resultados de acordo com uma condição específica;
    Execute a consulta e verifique os resultados.
'''
