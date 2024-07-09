faturamento = 1000
custo = 8800

lucro = faturamento - custo

# if condicao (comparacao):
    # tudo que voçê quer que aconteça se a condição for VERDADEIRA
# else 
   # tudo o que voçê quer que aconteça se a condição for FALSA
# ! = diferente ; (==) = igual
if lucro >= 0:
    print("Lucro", lucro)
else:
    print("Prejuízo!!!")
    print(lucro)


# produtos = ["iphone", "ipad", "airpod", "tv", "pc"]
# novo_produto = input("Digite aqui um produto:")
# novo_produto = novo_produto.lower()
# if novo_produto in produtos:
#     print("Produto já cadastrado")
# else:
#     print("Produto cadastrado com sucesso")
#     produtos.append(novo_produto)

# print(produtos)

# acima de 15000 -> 500 de bonus
# acima de 10000 -> 150 de bonus
# acima de 5000 -> 50 de bonus
# vendas da empresa > 50000
# vendas = 12000
# if vendas > 15000:
#     bonus = 500
# # (elif )caso contrario, se for maior que 10.000
# elif vendas > 10000:
#     bonus = 150
# elif vendas > 5000:
#     bonus = 50
 
# else:
#     bonus = 0
# print("Bonus", bonus)    


# verificar se as duas condições são verdadeiras
vendas = 11000
vendas_empresa = 40000
meta_empresa = 50000

if vendas > 15000 and vendas_empresa > meta_empresa:
    bonus = 500
elif vendas > 10000 and vendas_empresa > meta_empresa:
    bonus = 150
elif vendas > 5000 and vendas_empresa > meta_empresa:
    bonus = 50
else:
    bonus = 0
print("Bonus1", bonus)

# verificar se uma das condições é verdadeira
vendas = 11000
vendas_empresa = 40000
meta_empresa = 50000

if vendas > 15000 or vendas_empresa > meta_empresa:
    bonus = 500
elif vendas > 10000 or vendas_empresa > meta_empresa:
    bonus = 150
elif vendas > 5000 or vendas_empresa > meta_empresa:
    bonus = 50
else:
    bonus = 0
print("Bonus2", bonus)