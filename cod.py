faturamento = 1000
custo = 300

novas_vendas = 330
faturamento = faturamento + novas_vendas

taxa_imposto = 0.1
mensagem = 'O faturamento foi de '
teve_lucro = False

imposto = taxa_imposto * faturamento
print ('Faturamento' , faturamento)
print ('Custo' , custo)
print ('Lucro' , faturamento - custo - imposto)
print (mensagem, faturamento)


