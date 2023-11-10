pop = int(input("Informe a população da cidade: "))
me = int(input("Informe a margem de erro(%): "))

e = me / 100
z = 1.96  # 95%
p = 0.5  # 50

n = (z**2 * p * (1 - p)) / (e**2)

print(
    f"Para a cidade com uma população de {pop} habitantes e uma margem de erro de {me}%, são necessárias aproximadamente {n:.0f} entrevistas."
)


"""
n = tamanho da amostra da população a ser obtida

N = tamanho da população total

o = desvio padrão da população

p: Estimativa da proporção da população que possui a característica que você está medindo.(50/50 no caso)

Z = nível de confiança

e = margem de erro

Fórmula sem Correção de População Finita:

N = (Z^2 * p * (1 - p)) / E^2


Fórmula com Correção de População Finita

[z2 * p(1-p)] / e2 / 1 + [z2 * p(1-p)] / e2 * N]

"""
