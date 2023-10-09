'''Atividade: Listando cubos
➔ O QUE FAZER?
Crie um novo arquivo .py:
1. Elabore um algoritmo que use uma list comprehension para gerar uma lista
dos cubos dos dez primeiros números ímpares.'''

x = [n **3 for n in range(1,20,2)]
print(x)