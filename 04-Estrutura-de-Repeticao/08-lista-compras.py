compras = ["banana, maça, uva"]

produto = input("Digite um produto (ou 'fim' para terminar)")

while produto != "fim":
    compras.append(produto)

    produto = input("Digite um produto (ou 'fim' para terminar)")

    print(compras)

print("lista de compras: ")

for ListaProdutos in compras:
    print('-', ListaProdutos)