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
### 1.Clone o repositório

```bash
git clone https://github.com/seuusuario/seu-repo.git
cd seu-repo

### 2. Instale as dependências
- Certifique-se de estar usando o Python 3. Depois, execute:

pip install -r requirements.txt

### 3.Prepare sua planilha
Crie ou edite um arquivo .ods contendo, no mínimo, as colunas
 - Nome --> Nome do destinatário (para saudação personalizada)
 - Email ---> E-mail para o qual a mensagem será enviada

## 4. Configure as credenciais de e-mail
Este projeto utiliza autenticação via senha de aplicativo(exigida pelo Gmail).
Você deve exportar a senha como variável de ambiente ou editá-la diretamente no script(não recomendado )

- Usando variáveis de ambiente (recomendado):
 No Windows (CMD)
 set Senha_email = sua_senha_de_app

- Editar diretamente no enviar_emails.py:
    senha = 'sua_senha_de_app'