lista_precos = [1500, 1000, 800, 3000]

total_imposto = 0  # acumulado

# def calcular_imposto(preco):
#     if preco > 2000:
#         imposto = preco * 0.2
#     elif preco > 1000: # caso contrario
#         imposto = preco * 0.15
#     else:
#         imposto = preco * 0.1
#     print(f"Preço {preco}, Imposto: {imposto}")
#     return imposto



# for preco in lista_precos:
#     imposto = calcular_imposto(preco)
#     total_imposto = total_imposto + imposto
# print(total_imposto)


def calcular_imposto(preco, aliquota1=0.2, aliquota2=0.15, aliquota3=0.1):
    if preco > 2000:
        imposto = preco * aliquota1
    elif preco > 1000: # caso contrario
        imposto = preco * aliquota2
    else:
        imposto = preco * aliquota3
    print(f"Preço {preco}, Imposto: {imposto}")
    return imposto



for preco in lista_precos:
    imposto = calcular_imposto(preco, 0.25, 0.17, 0.12)  # por posição 
    total_imposto = total_imposto + imposto
print(total_imposto)

def calcular_imposto2(preco, ir=0.275, csll=0.035, iss=0.05):
    imposto_ir = preco * ir
    imposto_csll = preco * csll
    imposto_iss = preco * iss
    return imposto_ir, imposto_csll, imposto_iss

resposta = calcular_imposto2(1000)
print(resposta)
