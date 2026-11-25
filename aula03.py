#inputs pedir ua informação ao usuário
email= input("Digite seu email: ") #input sempre retorna uma string
nome= input("Digite seu nome: ")
print(nome, email)
#input sempre a informação é do tipo string, mesmo que seja um número, para converter para inteiro ou float é necessário usar int() ou float()
print(f"{nome},Verifique seu email {email} que enviamos um link de confirmação")

#lista é definida por colchetes []
vendas = [100, 50, 14, 20, 700]
total_vendas = sum(vendas) #sum() soma todos os elementos da lista  
print(f"Total de vendas: {total_vendas}")
quantidade_vendas = len(vendas) #len() retorna a quantidade de elementos da lista
print(f"Quantidade de vendas: {quantidade_vendas}")
#max() retorna o maior valor da lista
maior_venda = max(vendas)
#min() retorna o menor valor da lista
menor_venda = min(vendas)

#pegar o valor de uma posição da lista, a primeira posição é 0,sempre que a lista seja definida por colchetes [] 0 e q primeira posição, 1 a segunda posição e assim por diante -1 e a ultima posição, -2 a penúltima posição e assim por diante 
lista_produtos = ["camisa", "calça", "meia", "sapato"]

produto_procurado = input("Digite o produto que deseja procurar: ")
produto_procurado = produto_procurado.lower() #converte para minúsculo

print(f"{produto_procurado}" in lista_produtos) #verifica se o elemento está na lista, retorna True ou False

#adicionar elementos na lista, append() adiciona no final da lista
lista_produtos.append("camisa")
print(lista_produtos)

#remover elementos da lista, remove() remove o elemento da lista, se houver mais de um elemento igual, remove o primeiro encontrado
lista_produtos.remove("camisa")
print(lista_produtos)

lista_produtos.pop() #pop(0) remove o último elemento da lista
print(lista_produtos)

#editar elementos da lista, basta acessar a posição do elemento e atribuir um novo 
# valor
preços = [1000, 1500, 3500]
preços[0] = preços[0] * 1.5 #adiciona 100 ao primeiro elemento da lista
print(preços)

#contar quantas vezes um elemento aparece na lista, count() retorna a quantidade de vezes que o elemento aparece na lista
lista_produtos = ["camisa", "calça", "meia", "sapato","camisa","camisa"]
print(lista_produtos.count("camisa")) #retorna 3

#ordenar a lista, sort() ordena a lista em ordem crescente, se quiser em ordem decrescente, basta passar o parâmetro reverse=True
vendas.sort()#ordena a lista em ordem decrescente
print(vendas)

#todos esses metodos editam a lista original, ou seja, a lista original é alterada, se quiser manter a lista original, é necessário criar uma nova lista com os elementos desejados