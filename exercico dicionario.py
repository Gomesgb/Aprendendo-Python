dic_precos = {"celular": 1500,
               "camera": 1000,
                 "fone de ouvido": 800,
                   "monitor": 2000}

produto_procurado = input("Digite um produto")
produto_procurado = produto_procurado.lower()

if produto_procurado in dic_precos:
    preco = dic_precos[produto_procurado]
    print(f"Produto {produto_procurado}, Preço: {preco}")
else:
    print("Produto não encontrado, tente novamente")