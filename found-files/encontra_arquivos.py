import os
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
    except Exception as e:
        print(f"Erro ao converter SID para usuário: {e}")
        return sid
    
# Função para encontrar o diretório de reciclagem do Windows
def returnDir():
    dirs = ['C:\\Recycler\\', 'C:\\Recycled\\', 'C:\\$Recycle.bin\\']
    for recycleDir in dirs:
        if os.path.isdir(recycleDir):
            return recycleDir
    return None

# Função para encontrar e listar os arquivos excluídos no diretório de reciclagem
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
                print('\n⇾ Lista de arquivos excluídos do usuário: ' + str(user))
                for file in files:
                    print('Arquivo encontrado: ' + str(file))
            except PermissionError:
                print(f"Permissão negada para acessar: {path}")
            except Exception as e:
                print(f"Erro ao listar arquivos em {path}: {e}")

# Função principal do programa
def main():
   # Obtém o diretório de reciclagem
    recycledDir = returnDir()
    # Encontra e lista os arquivos excluídos no diretório de reciclagem
    findRecycled(recycledDir)

if __name__ == '__main__':
    main()
