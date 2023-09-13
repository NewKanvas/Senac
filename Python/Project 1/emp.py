# Tem quer ter essa informação previa
saldo = 3000
renda = 1320

while True:
    # Fazer menu, esse codigo e apenas a logica.

    emp = float(input("Digite o valor desejado (ou 0 para sair): "))

    if emp == 0:
        print("Saindo...")
        break

    if emp > renda * 2:
        print("Valor negado. O valor solicitado excede o dobro da renda.")
    else:
        print("Valor aceito.")
        saldo += emp
        juros = (emp * (20 / 100)) + emp
        print(
            f"Seu emprestimo de {emp}R$ foi adcionado a sua conta.\nSeu saldo é de {saldo}.\nVocê tera que pagar {juros}R$"
        )
