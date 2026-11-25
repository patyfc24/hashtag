# exemplo para novos produtos cadastrados sem aumento

# 📦 Produtos que JÁ existem — esses vão receber o aumento
dic_produtos = {"airpod": 2000, "iphone": 9000, "macbook": 6000, "apple_watch": 12000}

# 🔒 Guardamos os nomes dos produtos ANTES de adicionar o novo
produtos_antigos = list(dic_produtos.keys())

# 🆕 Adicionando um produto NOVO — SEM aumento
nome_produtos = input("Nome do produto: ")
preço_produtos = input("Preço do produto: ")

nome_produtos = nome_produtos.lower()
preço_produtos = float(preço_produtos)

dic_produtos[nome_produtos] = preço_produtos

# 🔁 Aumento de 10% — SÓ nos produtos antigos
print("\n📊 Aumento de 10% nos produtos antigos:")
for produto in produtos_antigos:
    novo_preco = dic_produtos[produto] * 1.1
    dic_produtos[produto] = novo_preco
    print(f"✅ {produto}: R$ {novo_preco:.2f}")

# ✅ O produto NOVO mantém o preço normal
print(f"\n🆕 Produto novo: {nome_produtos} — R$ {preço_produtos:.2f} (sem aumento)")
print("\n✅ Lista final:", dic_produtos)
