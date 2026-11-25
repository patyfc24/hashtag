
#sempre que voce tem informaçoes, que voce quer que essas informaçoes tenham um rotulo associado, voce vai usar a estrutura de um dicionario
dic_produtos = {"airpod": 2000,"iphone": 9000,"macbook": 6000,"apple_watch": 12.000 }

#pegar um elemento
print(dic_produtos["airpod"]) #entre colchetes o que deseja consultar informçao rotulada
dic_produtos["airpod"] =dic_produtos["airpod"] * 1.3
print(dic_produtos)

# quantidade de itens 
print(len(dic_produtos))

# retirar um item do dicionario
dic_produtos.pop("airpod")
print(dic_produtos)

# adicionar um item no dicionario 
dic_produtos["ipad"] = 4000
print(dic_produtos)

# dic so pode ter uma chave ele nao deixar ter 2 x o mesmo produto

# verificar se um item existe no dicionario
if "airpod" in dic_produtos:
    print(" Existe no dicionario")
else:
    print("Nao existe no dicionario")

# verificar se um valor existe nos valores do dicionario
if 9000 in dic_produtos.values():# pegar os valores transformando numa lista de itens 
    print("Existe")
else:
    print("Nao existe")

nome_produto = input("Nome do produto: ")
preço_produto = input("Preço do produto: ")

# cadastrar novo produto(se o produto não existir)
# caso o produto exista ele vai editar o produto


# alem disso : o programa tem que atualizar o preço de todos os produtos para os novos valores que são 10% a mais que o preço original
