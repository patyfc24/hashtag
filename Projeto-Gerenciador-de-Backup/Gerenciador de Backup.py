import shutil
import os
from datetime import date
from tkinter.filedialog import askdirectory

# 📂 Escolher a pasta para fazer backup
nome_pasta_selecionada = askdirectory()
print("📁 Pasta selecionada:", nome_pasta_selecionada)

# 📋 Listar arquivos da pasta
lista_arquivos = os.listdir(nome_pasta_selecionada)
print("📋 Arquivos encontrados:", lista_arquivos)

# 📅 Pegar a data de hoje
data_atual = date.today().strftime("%d-%m-%Y")

# 📂 Criar pasta de backup com a data
nome_pasta_backup = f"backup_{data_atual}"
nome_completo_pasta_backup = os.path.join(nome_pasta_selecionada, nome_pasta_backup)

if not os.path.exists(nome_completo_pasta_backup):
    os.mkdir(nome_completo_pasta_backup)
    print(f"✅ Pasta criada: {nome_pasta_backup}")
else:
    print(f"✅ Pasta já existe: {nome_pasta_backup}")

# 🔁 Copiar cada arquivo
for arquivo in lista_arquivos:
    caminho_origem = os.path.join(nome_pasta_selecionada, arquivo)
    caminho_destino = os.path.join(nome_completo_pasta_backup, arquivo)
    
    # ✅ Só copia se for um arquivo (não copia pastas)
    if os.path.isfile(caminho_origem):
        shutil.copy2(caminho_origem, caminho_destino)
        print(f"✅ Copiado: {arquivo}")

print("\n🎉 Backup concluído com sucesso!")

