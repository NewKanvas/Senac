"""
A função deve exibir uma frase simples, como Brasília está localizada no país Brasil.
2. Forneça um valor default ao parâmetro que representa o país.
3. Chame sua função para três cidades diferentes em que pelo menos uma delas não esteja
no país default.
4. A intenção é que testem os diferentes tipos de argumentos e parâmetros que vimos ainda
há pouco.
"""

def f(x,y,z):
    print(f"{x[z]} está localizada no país {y[z]}")

a = 0
b = ["Brasília","Tokyo","Chernobyl"]
c = ["Brasil", "Japão", "Ucrânia"]

while a != 3:
    f(b,c,a)
    a = a+1
    

