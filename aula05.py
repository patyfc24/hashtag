# for 
lista_vendas = [1000, 500, 800, 1500, 2000, 2300]
meta = 1200
percentual_bonus = 0.1

for venda in lista_vendas:#lendo as linhas de codigo,para cada venda dentro da minha  lista de vendas,se a venda for maior ou igual a meta, então o bonus e igual a percentual_bonus vezes a venda, caso contrario o bonus e igual a 0 exibi pra mim o valor do bonus
    if venda >= meta:
        bonus = percentual_bonus * venda
        print(f"Bonus: {bonus}")
    else:
        bonus = 0
        print(f"Bonus: {bonus}")

#for i in range(10):#para cada item uma lista de item
    #print("Se escreve no canal", i) 
#for venda in lista_vendas:#tudo que voce quer que seja executado varias vezes voce vai colocar dentro do for  com tab para dentro
  #  print(f"Vendas: {venda}")#para cada venda na lista de vendas, ele vai imprimir o valor da venda
 #   print("proximo item da lista")
