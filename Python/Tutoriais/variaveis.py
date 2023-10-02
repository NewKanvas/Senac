
counter = 100          # Um número inteiro
miles   = 1000.0       # Um número de ponto flutuante
name    = "João"       # Uma string

#Numbers

var1 = 1
var2 = 10

#Strings

str = "Hello World!"

print (str)          # Imprime a string completa
print (str[0])       # Imprime o primeiro caracter da string
print (str[2:5])     # Imprime do 3º caracter ate o 5º
print (str[2:])      # Imprime apartir do 3º caracter
print (str * 2)      # Imprime 2 vezes a string
print (str + "TEST") # Concatena uma string a outra

''' Resultado
Hello World!
H
llo
llo World!
Hello World!Hello World!
Hello World!TEST
'''

#Listas
'''
Contem varios itens separados por virgula, e chamada com [], as listas pode conter itens de diferentes tipos.
'''
lista = [ 'abcd', 786 , 2.23, 'john', 70.2 ]
listam = [123, 'john']

print (lista)          # Imprime a lista por completo
print (lista[0])       # Imprime o primeiro elemento da lista
print (lista[1:3])     # Imprime do 2º element ate o 3º elemento
print (lista[2:])      # Imprime apartir do 3º elemento
print (listam * 2)     # Imprime 2 vezes a lista
print (lista + listam) # Concatena as duas lsitas

'''Resultado
['abcd', 786, 2.23, 'john', 70.2]
abcd
[786, 2.23]
[2.23, 'john', 70.2]
[123, 'john', 123, 'john']
['abcd', 786, 2.23, 'john', 70.2, 123, 'john']
'''

#Tuple

'''
Funciona igual a lista, porem utiliza () ao inves do [], a tupla não pode ser  atualizadas. Pode se entender como uma lista de "Apenas leitura".
'''

tuple = ( 'abcd', 786 , 2.23, 'john', 70.2  )
tuplem = (123, 'john')

#Dictionary
'''
Chamados por {}, consistem de pares, o primeiro valor normalmente e chamado de "dicitionary key" esse valor pode ser quase qualquer tipo de
valor geralmente é uma string ou um numero, por outro lado o outro segundo e chamado de "Valor" que pode ser qualquer tipo arbritario...
'''

dict = {}
dict['um'] = "Este é o um"
dict[2] = "Este é o dois"

dictm = {'name': 'john','code':6734, 'dept': 'sales'}


print (dict['um'])     # Imprime o "Valor" da "Chave" "um"
print (dict[2])        # Imprime o "Valor" 2
print (dictm)          # Imprime o Dicionario completo
print (dictm.keys())   # Imprime todas as "Chaves"
print (dictm.values()) # Imprime todos os "Valores"

'''Resultado
Este é o um
Este é o dois
{'name': 'john', 'code': 6734, 'dept': 'sales'}
dict_keys(['name', 'code', 'dept'])
dict_values(['john', 6734, 'sales'])
'''