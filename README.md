# Bloqueador de Sites

Este projeto é um Bloqueador de Sites desenvolvido em Python utilizando a biblioteca Tkinter para criar uma interface gráfica simples e amigável. O objetivo do projeto é permitir que o usuário bloqueie ou desbloqueie o acesso a sites no computador, modificando o arquivo `hosts` do sistema.

## **Funcionalidades**
- **Bloqueio de sites:** Adiciona URLs ao arquivo `hosts`, redirecionando para `127.0.0.1` e impedindo o acesso.
- **Desbloqueio de sites:** Remove URLs específicas do arquivo `hosts`, restaurando o acesso.
- **Visualizar sites bloqueados:** Lista todos os sites atualmente bloqueados em uma janela separada.

## **Requisitos**
Este projeto requer permissões administrativas para modificar o arquivo `hosts`. É necessário rodar o programa com privilégios de administrador.

### **Bibliotecas utilizadas**
- **tkinter:** Para a criação da interface gráfica.
- **elevate:** Para elevação de privilégios administrativos.

### **Como instalar as dependências**
Certifique-se de que o Python 3 está instalado em sua máquina e instale a biblioteca `elevate` executando:
pip install elevate

# Como usar
Insira os URLs dos sites que deseja bloquear ou desbloquear no campo de texto.
Clique em "Bloquear Site" para adicionar o site à lista de bloqueios ou em "Desbloquear Site" para removê-lo.
Utilize o botão "Ver Sites Bloqueados" para visualizar os sites atualmente bloqueados.

# Avisos
Este programa modifica o arquivo hosts do sistema. É recomendável criar um backup manual do arquivo antes de usar a aplicação.
Bloquear sites usando este método afeta todo o computador. Certifique-se de que você realmente deseja bloquear os sites informados.

# Licença
Este projeto está licenciado sob a Licença MIT. Veja o arquivo LICENSE para mais detalhes.
