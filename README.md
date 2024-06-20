# AutomatizaEmail

AutomatizaEmail é um projeto em Python que permite automatizar o envio de e-mails utilizando o protocolo SMTP. Este script permite enviar e-mails para múltiplos destinatários e registra o histórico dos e-mails enviados em um arquivo CSV.

## Funcionalidades

- Envio de e-mails para múltiplos destinatários
- Registro de e-mails enviados em um arquivo CSV
- Exibição do histórico de e-mails enviados
- Menu interativo para enviar e-mails ou visualizar o histórico

## Pré-requisitos

Antes de começar, certifique-se de ter o Python 3.x instalado. Você pode baixar e instalar o Python no [site oficial](https://www.python.org/).

## Instalação

1. Clone o repositório para o seu computador:

   ```sh
   git clone https://github.com/seu-usuario/automatizaemail.git
   cd automatizaemail
2. Verifique se o pip está instalado e atualizado:
   ```sh
    python -m ensurepip --upgrade
3. Instale as bibliotecas necessárias. As bibliotecas smtplib, email.mime, csv, os e datetime são parte da biblioteca padrão do Python, então não é necessário instalar nada adicional.

## Configuração
Abra o arquivo main.py e substitua as variáveis email_user e email_password com suas credenciais de e-mail.
1. Credenciais:
   ```sh
   email_user = 'seu_email@gmail.com'
   email_password = 'sua_senha_de_aplicativo'
Nota: Para contas Gmail, você precisará criar uma senha de aplicativo. Siga essas instruções para gerar uma senha de aplicativo e usar em vez da sua senha de e-mail.

## Uso
1. Para executar o script, use o seguinte comando:
   ```sh
   python aut.py
O menu interativo será exibido, permitindo que você escolha entre enviar e-mails ou visualizar o histórico de e-mails enviados.

## Estrutura do Projeto:
   ```sh
    automatizaemail/
    │
    ├── email_log.csv         # Arquivo CSV onde os logs dos e-mails enviados são armazenados
    ├── main.py               # Script principal contendo o código do automatizador de e-mails
    └── README.md             # Arquivo de documentação (este arquivo)
