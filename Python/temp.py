def calculaSalarioLiquido(salarioBruto):

    inss = salarioBruto * 0.08

    impostoDeRenda = salarioBruto * 0.11

    sindicato = salarioBruto * 0.05

    print('Salario Bruto: {}'.format(salarioBruto))

    print('Valor de INSS:  {}'.format(inss))

    print('Valor de IR: {}'.format(impostoDeRenda))

    print('Sindicato: {}'.format(sindicato))

    return salarioBruto - inss - impostoDeRenda - sindicato

def calcularSalario(salarioHora, horasTrab):

    salarioBruto = salarioHora * horasTrab

    return salarioBruto

salarioHora = int(input('Insira o salário por hora do funcionário: '))

horasTrab = int(input('Insira as horas trabalhadas no mês: '))

salario = calcularSalario(salarioHora,horasTrab)

salarioLiquido = calculaSalarioLiquido(salario)

print('Salário líquido: {}'.format(salarioLiquido))