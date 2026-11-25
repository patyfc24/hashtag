faturamento = 1200 #variavel para guarda dados
#numeros inteiro 1200exp
custo = 750.0 #tipo float 750.32exp numeros com casas decimais

novas_vendas = 100
faturamento = faturamento + novas_vendas

imposto= faturamento * 0.1

lucro = faturamento - custo - imposto
margem_lucro = lucro / faturamento 

print("faturamentofoi de ", faturamento)#apenas teto se colaca entre aspas
print("faturamentofoi de ", custo)
print("lucro foi de ", lucro)
print("margem de lucro foi de ", round(margem_lucro, 2))#round arredonda o valor para 2 casas decimais

print("O faturamento da loja foi de tanto")#varriavel string  texto

#Mode->% resto da divisao
print(10%3) #resto da divisao 10/3 = 3 resto 1
tempo_contrato = 170
tempo_anos =170/12
print("tempo de contrato em anos", int(tempo_anos)) #int converte para inteiro
tempo_meses =170%12
print("tempo em meses", tempo_meses)