#funçoes, quando vc cria uma função vc organiza seu codigo
lista_precos =[1500, 1000, 800, 3000]
#imposto
#aliquota1 - IR  - 2.0, se o preço do produto for ate 2000,acima disso a aliquota é de 0.3
#aliquota2 - ISS - 0.15
#ALIQUOTA3 - CSLL - 0.05
#xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
#função
#def + nome_da_funçao + dentro do () todas as informaçoes pra ela funcionar
def calcula_imposto_total(preco):  # criar função usa palavra def
    if preco <= 2000:
        imposto_ir = 0.2 * preco
    else:
        imposto_ir = 0.3 * preco

    imposto_iss = 0.15 * preco
    imposto_csll = 0.05 * preco
    imposto_total = imposto_ir + imposto_iss + imposto_csll
    return imposto_total # devolve a resposta imposto total return
#xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
#fim da funçao
for preco in lista_precos:
    imposto_total = calcula_imposto_total(preco)
    print(f"Imposto total sobre o produto de R${preco}: R${imposto_total}")


nova_lista_produtos = [3000, 5000, 6000, 7000]
for preco in nova_lista_produtos:
    imposto_total = calcula_imposto_total(preco)
    print(f"Imposto total sobre o produto de R${preco}: R${imposto_total}")

#detalhes impostantes: funçoes precisam de informaçoes pra elas funcionarem, importante: as variaveis que voce cria dentro de funçao elas so exitem dentro da funçao