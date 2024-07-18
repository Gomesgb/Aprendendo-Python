# for i in range(10):
#     print("Se increva do canal")

# for item in lista:
        # o que eu quero que seja executado várias vezes

lista_precos = [1500, 1000, 800, 2000]
imposto = 0.1

# for preco in lista_precos:
#     imposto = preco * 0.1
#     print(f"Preço {preco}, Imposto: {imposto}")
#     print("Terminou de rodar 1 item")

# regra do imposto
# preço até 1000 -> imposto é de 10%
# preço maior que 1000 -> imposto é de 15%

# for preco in lista_precos:
#     if preco > 1000:
#         imposto = preco * 0.15
#     else:
#         imposto = preco * 0.1
#     print(f"Preço {preco}, Imposto: {imposto}")
#     print("Terminou de rodar 1 item")


total_imposto = 0  # acumulado

for preco in lista_precos:
    if preco > 1000:
        imposto = preco * 0.15
    else:
        imposto = preco * 0.1
       # print(f"Preço {preco}, Imposto: {imposto}")
    total_imposto = total_imposto + imposto
print(total_imposto)