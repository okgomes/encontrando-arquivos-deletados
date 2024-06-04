Este é um programa em Python projetado para encontrar e listar arquivos excluídos presentes nos diretórios de reciclagem do sistema operacional Windows. Ele utiliza a biblioteca winreg para converter identificadores de segurança (SIDs) em nomes de usuários e os para manipulação de arquivos e diretórios. Ao ser executado, o programa procura por diretórios de reciclagem padrão (C:\\Recycler\\, C:\\Recycled\\ e C:\\$Recycle.bin\\) e lista os arquivos encontrados em cada diretório, mostrando o nome de usuário associado a cada conjunto de arquivos.

Funcionalidades:

৹ Localiza automaticamente os diretórios de reciclagem do Windows.
৹ Converte SIDs em nomes de usuários para identificar o proprietário de cada conjunto de arquivos.
৹ Lista os arquivos excluídos encontrados em cada diretório de reciclagem, junto com o nome de usuário associado.

Como Usar:

৹ Clone o repositório para o seu ambiente local.
৹ Execute o script main.py usando Python 3.
৹ O programa encontrará automaticamente os diretórios de reciclagem e listará os arquivos excluídos, mostrando o nome de usuário associado a cada conjunto de arquivos.
