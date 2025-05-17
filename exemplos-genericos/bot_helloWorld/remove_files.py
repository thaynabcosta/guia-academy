import os
from constants import *

def remove_txt():
    try:
        if os.path.exists(FILE_NAME):
            os.remove(FILE_NAME)
            print(f"Arquivo excluído: {FILE_NAME}")
        else:
            print("O arquivo não existe.")
    except Exception as e:
        print(f"Erro ao tentar excluir o arquivo: {e}")
