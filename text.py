# formatacao de texto

nome = 'Jéssica Ewald'
print(nome.capitalize())  #Jessica ewald
print(nome.title())  #Jessica Ewald

# especiais - formatacao numerico, letras e numeros
faturamento = 1000
custo = 330
lucro = faturamento - custo
margem = lucro / faturamento
print (f'Margem: {margem:.1%}') #porcentual
print(f'Faturamento: R${faturamento:,.2f}, Custo:{custo:,.2f}, Lucro: {lucro:,.2f}') #formatacao numerica
# recomendado essa formatacao no final
print(f'Faturamento: R${faturamento:,.2f}\n Custo:{custo:,.2f}\n Lucro: {lucro:,.2f}') # caracter que representa o enter \n

# ferramentas de texto
# selecao de pedacos
email = 'email.falso@gmail.com'

print (email.lower()) #funcao de texto que deixa em minusculo
print (email.find('@')) #procura indice  # -1, se caso nao encontrar o elemento. Se encontrar: a posicao
#elemento e cada posicao da variavel, comeca contando do 0
print (email[11])
posicao = email.find ('@')
servidor = email [11:] #da posicao ate o final
print (servidor)
servidor = email [:11] #da posicao ate o inicioo
print(servidor)
servidor = email [ posicao+1:] #da posicao posterior

tamanho=len (email)
print (tamanho) #quantidade de letras

email_trocado = email.replace ('gmail.com', 'hotmail.com') # troca informacoes
print (email_trocado)









