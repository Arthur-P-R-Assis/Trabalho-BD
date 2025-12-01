Sistema de Gerenciamento de Relatórios VETSYS
Este projeto implementa um console de relatórios para o sistema de clínica veterinária VETSYS, acessando diretamente o banco de dados PostgreSQL. O programa cumpre o requisito de apresentar um menu com acesso a três consultas gerenciais complexas.

Tecnologias Utilizadas
Linguagem: Python 3

Driver DB: psycopg2-binary (Para conexão nativa com PostgreSQL)

Interface: tabulate (Para formatação limpa e organizada dos resultados no console)

Como Rodar o Programa
Para executar o programa, você precisa ter o Python 3 instalado e acesso ao servidor PostgreSQL (Aiven).

1. Estrutura de Arquivos
Certifique-se de que os arquivos main.py, database.py e config.py estão no mesmo diretório.

2. Configuração do Banco de Dados
Você deve editar o arquivo config.py e substituir as placeholders pelas suas credenciais reais de conexão ao banco de dados PostgreSQL (Host, Porta, Usuário e Senha).
DB_CONFIG = {
    "host": "SEU_HOST",
    "database": "defaultdb",
    "user": "SEU_USUARIO",
    "password": "SUA_SENHA_SECRETA",
    "port": "SUA_PORTA",
    "sslmode": "require"
}

3. Instalação das Dependências
Instale as bibliotecas necessárias usando o pip e o arquivo requirements.txt:
pip install -r requirements.txt

4. Execução
Após configurar a conexão, execute o arquivo principal (main.py) via terminal:
python main.py

O programa exibirá um menu interativo, permitindo a seleção dos relatórios.
