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
Funciona igual a lista, porem utiliza () ao inves do [], a tupla não pode ser  atualizadas. Pode se entender como uma lista de "
'''