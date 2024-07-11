vendas = [100, 50, 130, 80, 120, 200]

print(vendas[-1])

total_vendas = sum(vendas)
print(total_vendas)
quantidade = len(vendas)
print(quantidade)
valor_max = max(vendas)
valor_min = min(vendas)
print(valor_max, valor_min)

posicao = vendas.index(130)
print(posicao)
print(vendas[:2])
print(vendas[2:])

produtos = ["iphone", "ipad", "airpod", "tv", "pc"]
precos = [400, 300, 250, 500, 600]
# produto_usuario = input("Digite o nome de um produto:")
# print(produto_usuario in produtos)
# editando um item
print("iphone" in produtos)
precos[0] = 450
# novo_preco = precos[0] * 1.1  aumentar 10% no valor do produto
print(precos)

# adicionar um item
produtos.append("macbook")
precos.append(1000)
print(produtos)
print(precos)

# remover um item
produtos.remove("macbook") # pelo valor
precos.pop(-1)  # pelo indice
print(produtos)
print(precos)

# inserir um valor
produtos.insert(1, "airpod")
print(produtos)

# contar valores
print(produtos.count("airpod"))

# ordenar
precos.sort()
print(precos)
