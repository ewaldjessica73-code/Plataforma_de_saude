# exercicio 1
# descubra o servidor e extraia
nome = 'Heitor Ewald'
email = 'email.heitor@gmail.com'

posicao = email.find('@')
servidor = email [posicao:]
print (email[12:])

# exercicio 2
# pegar o primeiro nome e print mensagem com usuario e email
posicao = nome.find (' ')
primeiro_nome = nome [:posicao]
print ('Olá ' + primeiro_nome)

#construa a mensagem: Enviamos um link de confirmaçao para o email e***@gmail.com
mensagem = f'Usuário {primeiro_nome} cadastrado com sucesso com o email: {email}' # mensagem com variavel
print (mensagem)

primeira_letra = email[0]
print (primeira_letra)
mensagem2 = f'Enviamos um link de confirmação para o email {primeira_letra}***{servidor}'
print (mensagem2)

