# sistema de consulta de preço

precos = [1500, 1000, 800, 2000]
produtos = ["celular", "camera", "fone de ouvido", "monitor"]

produto_procurado = input("Digite um produto")
produto_procurado = produto_procurado.lower()

if produto_procurado in produtos:
    posicao = produtos.index(produto_procurado)
    preco = precos[posicao]
    print(f"Produto: {produto_procurado}, Preço: {preco}")
else:
    print("Produto não encontrado, tente novamente")
