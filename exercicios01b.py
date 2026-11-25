#exemplo aumentando todos em 10% e nosvo que entrarem ja om valor acrescido
# LINHA 1 ↓ arrume aqui
dic_produtos = {"airpod": 2000, "iphone": 9000, "macbook": 6000, "apple_watch": 12000}

nome_produtos = input("Nome do produto: ")
preço_produtos = input("Preço do produto: ")

nome_produtos = nome_produtos.lower()
preço_produtos = float(preço_produtos)

dic_produtos[nome_produtos] = preço_produtos

# LINHA 8 ↓
for produto in dic_produtos:
    novo_preco = dic_produtos[produto] * 1.1   # ← LINHA 9: coloque espaço na frente
    dic_produtos[produto] = novo_preco           # ← LINHA 10: coloque espaço na frente
    print(novo_preco)                             # ← LINHA 11: coloque espaço na frente

print(dic_produtos)
