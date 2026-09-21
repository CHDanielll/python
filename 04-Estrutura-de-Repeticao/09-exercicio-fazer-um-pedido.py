quantidade = 0

produto = input ("Digite o produto que deseja pedir: ")

while produto != "sair":
    quantidade = quantidade + 1

    produto = input ("Digite outo produto: ")

print(f"Voce pediu {quantidade} produtos")
print ("Pedido finalizado!")