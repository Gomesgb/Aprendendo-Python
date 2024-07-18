produtos = ["iphone", "ipad", "airpod", "tv", "pc"]

while True:
    novo_produto = input("Digite aqui um produto:")
    novo_produto = novo_produto.lower()
    if "sair" == novo_produto:
        break

    if novo_produto in produtos:
     print("Produto já cadastrado")
    else:
     print(f"Produto {novo_produto} cadastrado com sucesso")
     produtos.append(novo_produto)

print(produtos)