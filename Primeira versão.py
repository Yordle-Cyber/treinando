repetir = "sim"
while repetir == "sim":
    salariobruto = float(input("insira o salário: "))
    print("INSS:")
    if salariobruto <= 1100.00:
        h = salariobruto * 0.075
        salariosemoinss = salariobruto - h
        print(f"valor retirado pelo INSS: {h:.2f} R$")
    elif salariobruto >= 1100.01 and salariobruto <= 2203.48:
        h = salariobruto * 0.09 - 16.50
        salariosemoinss = salariobruto - h
        print(f"valor retirado pelo INSS: {h:.2f} R$")
    elif salariobruto >= 2203.49 and salariobruto <= 3305.22:
        h = salariobruto * 0.12 - 82.60
        salariosemoinss = salariobruto - h
        print(f"valor retirado pelo INSS: {h:.2f} R$")
    elif salariobruto >= 3305.23 and salariobruto <= 6433.57:
        h = salariobruto * 0.14 - 148.70
        salariosemoinss = salariobruto - h
        print(f"valor retirado pelo INSS: {h:.2f} R$")
    else:
        h = 751.97
        salariosemoinss = salariobruto - h
        print(f"valor retirado pelo INSS: {h:.2f} R$")
    print("Salario Familia: ")
    if salariobruto <= 1503.25:
        filhos = int(input("Quantidade de filhos (menor de 14): "))
        totaladicionado = filhos * 51.27
        calculofinal = salariosemoinss + totaladicionado
        print(f"o Salario Familia é: {totaladicionado:.2f} R$")
    else:
        print("funcionario sem direito ao salário familia.")
    if salariosemoinss >= 1503.26 and salariosemoinss <= 1903.98:
        calculofinal = salariosemoinss
    print("IRRF: ")
    dependentes = int(input("Quantidade de dependentes:"))
    p = dependentes * 189.59
    m = salariosemoinss - p
    if m >= 1903.99:
        if m <= 2826.65:
            desconto = (m * 0.075) - 142.80
            calculofinal = salariosemoinss - desconto
            print(f"o valor retirado pelo IRRF: {desconto:.2f} R$")
        elif m >= 2826.66 and m <= 3751.05:
            desconto = (m * 0.15) - 354.80
            calculofinal = salariosemoinss - desconto
            print(f"o valor retirado pelo IRRF: {desconto:.2f} R$")
        elif m >= 3751.06 and m <= 4664.68:
            desconto = (m * 0.225) - 636.13
            calculofinal = salariosemoinss - desconto
            print(f"o valor retirado pelo IRRF: {desconto:.2f} R$")
        elif m >= 4664.68:
            desconto = (m * 0.275) - 869.36
            calculofinal = salariosemoinss - desconto
            print(f"o valor retirado pelo IRRF: {desconto:.2f} R$")
    else:
        calculofinal = salariosemoinss
        print("funcionário sem desconto IRRF")
    print("Vale Transporte: ")
    logico = (input("cliente deseja vale transporte? "))
    if logico == "sim":
        dias = int(input("insira a quantidade de dias úteis: "))
        passagem = float(input("insira o valor da passagem: "))
        valetransporte1 = dias * passagem * 2
        valetransporte2 = salariobruto * 0.06
        if valetransporte1 > valetransporte2:
            descontovale = valetransporte2
            print(
                f"o valor retirado pelo vale transporte é: {valetransporte2:.2f} R$"
            )
        else:
            descontovale = valetransporte1
            print(
                f"o valor retirado pelo vale transporte é: {valetransporte1:.2f} R$"
            )
        salariofinal = calculofinal - descontovale
    else:
        salariofinal = calculofinal
    print(f"o salário líquido do funcionário é: {salariofinal:.2f} R$")
    print("13º? ")
    decimo = input()
    if decimo == "sim":
        if m >= 1903.99:
            parcela = salariobruto / 2
            segundomes = parcela - desconto - h
            primeirom = salariofinal + parcela
            segundom = salariofinal + segundomes
        elif m <= 1903.98:
            parcela = salariobruto / 2
            segundomes = parcela - h
            primeirom = salariofinal + parcela
            segundom = salariofinal + segundomes
        else:
            print(" ")
    print(
        f"o valor bruto da parcela é: {parcela:.2f} R$, e com descontos: {segundomes:.2f} R$ \na soma do primeiro mes com decimo é: {primeirom:.2f} R$ e a soma da segunda parcela é: {segundom:.2f} R$"
    )
    repetir = input("\ndeseja fazer novamente? ")
    print("\n")
