#if condiçao:
    # código a ser executado se a condição for verdadeira
#else:
    # código a ser executado se a condição for falsa

vendas = 1500
meta = 1300

# > maior que
# < menor que
# >= maior ou igual a
# <= menor ou igual a
# == igual a
# != diferente de

if vendas > meta:
        print("vendedor ganha bônus") #sempre que usar if colocar tardizamento, ou seja, o código dentro do if deve estar indentado, ou seja, com 4 espaços ou 1 tabulação
        print(" Bateu a meta de vendas")
        bonus = 0.1 * vendas
        print(f"Bonus do vendedor: {bonus}")
else:
        print("vendedor não ganha bônus")
        print("Não bateu a meta de vendas")#tudo que estiver dentro do if ou else deve estar indentado, ou seja, com 4 espaços ou 1 tabulação

#2º cenario
vendas = 2100
vendas_empresa = 10000
meta_empresa = 20000
meta1 = 1300 #ganhar 10%
meta2 = 2000 #ganhar 13%

if vendas >= 2000 and vendas_empresa >= meta_empresa:#colocar : depois da condição do if, else e elif
    bonus = 0.13 * vendas
else:#caso contrário, ou seja, se a condição do if não for verdadeira,ele nao vendeu mais de 2000, então ele vai para o else
    if vendas >= 2100:
        bonus = 0.13 * vendas
    #else:
    #    bonus = 0
    elif vendas >= 1300 and vendas_empresa >= meta_empresa:#entre um if e else, podemos colocar quantos elif quisermos, ou seja, se a condição do if não for verdadeira, ele vai para o elif, se a condição do elif não for verdadeira, ele vai para o próximo elif, e assim por diante, até chegar no else
        bonus = 0.1 * vendas
    else:
        bonus = 0

print(f"Bonus: {bonus}")

lista_produtos = ["camisa", "calça", "meia", "sapato"]
produto_procurado = input("Digite o produto que deseja procurar: ")
produto_procurado = produto_procurado.lower() #converte para minúsculo

if produto_procurado in lista_produtos:#isso pode ser uma condiçao ou comparaçao, ou seja, se o produto procurado estiver na lista de produtos, ele vai entrar no if, caso contrário, ele vai para o else
    print(f"{produto_procurado} Produto no estoque")
else:
    print(f"{produto_procurado}  Não temos esse produto no estoque")