# exercícios

nome = "Luis Gomes Junior"
email = "emailfalso2@gmail.com"

# descubra o servidor do email
posicao = email.find("@")
servidor = email[posicao:]
print(servidor)
# pegar o 1° nome do usuario
posicao = nome.find(" ")
primeiro_nome = nome[:posicao]
print(primeiro_nome)
# contrua uma mensagem : Usuario primeiro_nome cadastrado com sucesso com o email tal
mensagem = f"Usuario {primeiro_nome} cadastrado com sucesso com o email: {email}"
print(mensagem)
# contrua uma mensagem: Enviamos um link de confirmação para o email e***@gmail.com
primeira_letra = email[0]
print(primeira_letra)
mensagem2 = f"Enviamos um link de confirmação para o email {primeira_letra}***{servidor}"
print(mensagem2)