# Envio automático de E-mails com Python
Este projeto automatiza o envio de e-mails personalizados utilizando uma planilha `.ods` com os dados

## Funcionalidades 
- Leitura de planilha `.ods` com nomes e e-mails
- Envio de e-mails em *formato HTML*
- Inclusão de *assinatura personalizada com imagem e links*
- Saudação personalizada com o nome do destinatário
- Envio de e-mails em lotes, com pausa entre os lotes
- Compatível com *conta Gmail* com autenticação por senha de app

## Tecnologias utilizadas

- Python 3
- pandas
- smtplib
- email(biblioteca padrão)
- odfpy (para leitura de ` .ods`)

## Estrutura do projeto

- enviar_emails.py #Scrip principal de envio
- ler_planilhas.py #Função que carrega os nomes e e-mails da planilha
- lista de emails.ods
- README.md
- requirements.txt

## Como usar