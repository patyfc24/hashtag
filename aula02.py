faturamento = 1000
custo = 700
lucro = faturamento - custo

print(f"Faturamento da empresa: {faturamento}, custo: {custo}, lucro: {lucro}")

email_cliente = "email_cliente@gmail.com"

# maiúsculo
email_cliente_maiusculo = email_cliente.upper()
print(email_cliente_maiusculo)

# minúsculo
email_cliente_minusculo = email_cliente.lower()
print(email_cliente_minusculo)

# encontra posição do @
print(email_cliente.find("@"))

# tamanho da string
print(len(email_cliente))

# pegar um caractere
print(email_cliente[8])
print(email_cliente[-2])

# fatiar parte do texto
print(email_cliente[4:10])

# trocar texto
print(email_cliente.replace("gmail", "hotmail"))

nome = "João da Silva"
print(nome.capitalize())
print(nome.title())

# SERVIDOR DO EMAIL ✅
posição_arroba = email_cliente.find("@") + 1
servidor = email_cliente[posição_arroba:]
print("Servidor:", servidor)

# SEPARAR NOME E SOBRENOME ✅
posiçao_espaco = nome.find(" ") + 1
sobrenome = nome[posiçao_espaco:]
print(primeiro_nome := nome[:posiçao_espaco - 1])
print(sobrenome)

# ✅ CORRIGIDO: calcular margem primeiro!
margem_lucro = lucro / faturamento
margem_lucro = round(margem_lucro, 2)
# ✅ CORRIGIDO: nome da variável completo
print(f"Faturamento da empresa:        R${faturamento:.2f}, custo:R$ {custo:,.2f}, lucro: R${lucro:,.2f}, margem: {margem_lucro:.2%}")
#nome da varialvel : codigo da formatação
