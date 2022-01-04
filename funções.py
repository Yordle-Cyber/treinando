def calcula_inss(valor):
    if valor <= 1100.00:
        return valor * 0.075
    elif valor >= 1100.01 and valor <= 2203.48:
        return valor * 0.09 - 16.50
    elif valor >= 2203.49 and valor <= 3305.22:
        return valor * 0.12 - 82.60
    elif valor >= 3305.23 and valor <= 6433.57:
        return valor * 0.14 - 148.70
    else:
        return 751.97

def calcula_salario_familia(qtd_filhos):
    return qtd_filhos * 51.27

def calcular_irrf(valor, dependentes):
    p = dependentes * 189.59
    m = valor - p
    if m >= 1903.99:
        if m <= 2826.65:
            return (m * 0.075) - 142.80
        elif m >= 2826.66 and m <= 3751.05:
            return (m * 0.15) - 354.80
        elif m >= 3751.06 and m <= 4664.68:
            return (m * 0.225) - 636.13
        elif m >= 4664.68:
            return (m * 0.275) - 869.36
        else:
            return 0
    else:
        return 0

def vale_transporte(dias, passagem, salario_bruto):
    valetransporte1 = dias * passagem * 2
    valetransporte2 = salario_bruto * 0.06
    if valetransporte1 > valetransporte2:
        return valetransporte2
    else:
        return valetransporte1

class decimo:
    def metodo_parcela_unica(salario, valor2, dependentes):
        decimo = salario * valor2 / 12
        desconto_inss = calcula_inss(decimo)
        print(f"Desconto INSS: R$ {desconto_inss:.2f}")
        desconto_irrf = calcular_irrf(decimo, dependentes)
        print(f"Desconto IRRF: R$ {desconto_irrf:.2f}")
        return decimo - desconto_inss - desconto_irrf

    def metodo_parcelado(salario, valor2, dependentes):
        decimo = salario * valor2 / 12
        desconto_inss = calcula_inss(decimo)
        print(f"Desconto INSS: R$ {desconto_inss:.2f}")
        salario_com_desconto = decimo - desconto_inss
        desconto_irrf = calcular_irrf(salario_com_desconto, dependentes)
        print(f"Desconto IRRF: R$ {desconto_irrf:.2f}")
        primeira_parcela = decimo / 2
        segunda_parcela = decimo / 2 - desconto_inss - desconto_irrf
        return (primeira_parcela, segunda_parcela)

def calcular_salario():
    salario_bruto = float(input("Insira o salário: "))
    dependentes = int(input('Informe a quantidade de dependentes: '))
    filhos = 0
    salario_familia = 0
    vl_inss = calcula_inss(salario_bruto)
    salario_familia = 0
    salario_menos_inss = salario_bruto - vl_inss
    valor_vale_transporte = 0

    vl_irrf = calcular_irrf(salario_menos_inss, dependentes)

    if salario_menos_inss <= 1503.25:
        filhos = int(input("Quantidade de filhos (menor de 14): "))
        salario_familia = calcula_salario_familia(filhos)

    logico = (input("Fucionário deseja vale transporte? "))
    if logico.lower() == "sim":
        dias = int(input("Insira a quantidade de dias úteis: "))
        passagem = float(input("Insira o valor da passagem: "))
        valor_vale_transporte = vale_transporte(dias, passagem, salario_bruto)
    else: print("")

    salario_liquido = salario_bruto - vl_inss - vl_irrf + salario_familia - valor_vale_transporte

    print(f"Salario Bruto: R$ {salario_bruto:.2f}")
    print(f"Desconto INSS: R$ {vl_inss:.2f} ")
    print(f"Desconto IRRF: R$ {vl_irrf:.2f} ")
    print(f"Valor para o salario familia: R$ {salario_familia:.2f} ")
    print(f"Desconto vale transporte: R$ {valor_vale_transporte:.2f} ")
    print(f"Salário Líquido: R$ {salario_liquido:.2f}")

    pergunta = (input("13º? "))
    if pergunta.lower() == "sim":
        meses = int(input("Insira a quantidade de meses trabalhado: "))
        pergunta1 = input("Deseja parcelado ou inteiro? ")
        if pergunta1.lower() == "parcelado":
            parcela1, parcela2 = decimo.metodo_parcelado(salario_bruto, meses, dependentes)
            print(f"Primeira parcela: R$ {parcela1:.2f}")
            print(f"Segunda parcela (com descontos): R$ {parcela2:.2f}")
            resultado1 = parcela1 + salario_liquido
            resultado2 = parcela2 + salario_liquido
            print(f"Primeira parcela com o mês: R$ {resultado1:.2f}")
            print(f"Segunda parcela com o mês: R${resultado2:.2f}")
        elif pergunta1.lower() == "inteiro":
            inteiro = decimo.metodo_parcela_unica(salario_bruto, meses, dependentes)
            print(f"o valor do décimo com descontos R$: {inteiro:.2f}")
            resultado = salario_liquido + inteiro
            print(f"soma com o mês: R$ {resultado:.2f}")
        else: print("")
