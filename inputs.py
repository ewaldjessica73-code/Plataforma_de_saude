

nome = input ('Diga seu nome: ')
email = input ('Digite aqui seu email: ')
print (nome)
print (email)


posicao = email.find('@')
servidor = email [posicao:]

posicao = nome.find (' ')
primeiro_nome = nome [:posicao]
print ('Olá ' + primeiro_nome)

mensagem = f'Usuário {primeiro_nome} cadastrado com sucesso com o email: {email}' # mensagem com variavel
print (mensagem)

primeira_letra = email[0]

mensagem2 = f'Enviamos um link de confirmação para o email {primeira_letra}***{servidor}'
print (mensagem2)