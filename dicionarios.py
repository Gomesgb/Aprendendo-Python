precos = [1500, 1000, 800, 2000]
produtos = ["celular", "camera", "fone de ouvido", "monitor"]

# dicionario é conjunto de elementos em que cada item é um conjunto de chave e valor
dic_precos = {"celular": 1500,
               "camera": 1000,
                 "fone de ouvido": 800,
                   "monitor": 2000}

# pegar um item
preco_celular = dic_precos["celular"]
print(preco_celular)

dic_precos["celular"] = 2000
print(dic_precos)

# adicionar item
dic_precos["iphone"] = 4500
print(dic_precos)

# deletar valor
dic_precos.pop("iphone")
print(dic_precos)

# tamanho
print(len(dic_precos))

print("televisao" in dic_precos)
print(dic_precos.keys())
print(1500 in dic_precos.values()) # procurar valor