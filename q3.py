nome = input("Digite seu nome: ")
quantidade = int(input("Quantos cadernos deseja comprar? "))
preco = float(input("Digite o preço de cada caderno: R$ "))

total = quantidade * preco

if total > 100:
    desconto = total * 0.10
    total = total - desconto
    print("Você recebeu 10% de desconto!")

print("Cliente:", nome)
print("Valor final: R$", total)