import os
import struct
from winreg import *

# Função para converter SID em nome de usuário
def sid2user(sid):
    try:
        key = OpenKey(HKEY_LOCAL_MACHINE,
                      r"SOFTWARE\Microsoft\Windows NT\CurrentVersion\ProfileList" 
                      + '\\' + sid)
        value, _ = QueryValueEx(key, 'ProfileImagePath')
        user = value.split('\\')[-1]
        return user
    except Exception:
        return sid

# Função para encontrar o diretório da Lixeira do Windows
def returnDir():
    dirs = ['C:\\Recycler\\', 'C:\\Recycled\\', 'C:\\$Recycle.Bin\\']
    for recycleDir in dirs:
        if os.path.isdir(recycleDir):
            return recycleDir
    return None

# Função para recuperar o nome original de arquivos excluídos
def get_original_filename(metadata_file):
    try:
        with open(metadata_file, "rb") as f:
            f.read(20)  # Pula os primeiros 20 bytes (dados internos)
            raw_name = f.read().decode("utf-16").strip("\x00")  # Lê o nome original
            return raw_name
    except Exception as e:
        return f"Erro ao recuperar nome: {e}"

# Função para listar arquivos excluídos e recuperar mais informações
def findRecycled(recycleDir):
    if recycleDir is None:
        print("Nenhum diretório de reciclagem encontrado.")
        return

    dirList = os.listdir(recycleDir)
    for sid in dirList:
        path = os.path.join(recycleDir, sid)
        if os.path.isdir(path):
            try:
                files = os.listdir(path)
                user = sid2user(sid)
                print(f'\n⇾ Arquivos excluídos do usuário: {user}')

                for file in files:
                    full_path = os.path.join(path, file)

                    if file.startswith("$I"):  # Se for um arquivo de metadados
                        original_name = get_original_filename(full_path)
                        print(f'📄 Nome original: {original_name}')
                    
                    elif file.startswith("$R"):  # Se for um arquivo real
                        print(f'📂 Arquivo recuperável: {file}')
            except PermissionError:
                print(f"⚠ Permissão negada para acessar: {path}")
            except Exception as e:
                print(f"❌ Erro ao listar arquivos em {path}: {e}")

# Função principal do programa
def main():
    recycledDir = returnDir()  # Obtém o diretório da Lixeira
    findRecycled(recycledDir)  # Lista os arquivos e exibe mais informações

if _name_ == '_main_':
    main()
