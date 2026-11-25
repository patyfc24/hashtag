import os
import os

# 📦 Lista todos os arquivos dentro da pasta "arquivos"
lista_arquivos = os.listdir("arquivos")

# 🔁 Para cada arquivo na lista...
for arquivo in lista_arquivos:
    # Verifica se é um arquivo .txt
    if ".txt" in arquivo:
        
        # Se tiver "22" no nome → move para pasta 2022
        if "22" in arquivo:
            de = f"arquivos/{arquivo}"
            para = f"arquivos/22/{arquivo}"  # ✅ pasta diferente!
            os.rename(de, para)
            print(f"✅ Movido: {arquivo} → 22")
        
        # Se tiver "23" no nome → move para pasta 2023
        elif "23" in arquivo:
            de = f"arquivos/{arquivo}"
            para = f"arquivos/23/{arquivo}"  # ✅ pasta diferente!
            os.rename(de, para)
            print(f"✅ Movido: {arquivo} → 23")


#import datetime
#import pyautogui
#pyautogui.press("win")
###print(os.listdir("arquivos"))
#print(datetime.date.today())
#pandas 
#openpyxl excel
#modulos 
#  bibliotecas pacote de codigos que vc instala no seu desketop 
# abrir renomear nomes de arquivos 
