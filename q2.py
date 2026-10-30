salario = 1800
horas_extras = 12
valor_hora = 25

total_extras = horas_extras * valor_hora
salario_total = salario + total_extras

if salario_total > 2000:
    salario_total = salario_total + 150

print("Salário final: R$", salario_total)