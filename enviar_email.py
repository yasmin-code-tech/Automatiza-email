import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from ler_planilha import carregar_emails

# Carrega a lista de emails
emails = carregar_emails()

# Configurações do e-mail
remetente = 'yasmin.jobs33@gmail.com'
senha = 'cfxg xrdl ahik ftcl'

smtp_server = 'smtp.gmail.com'
smtp_port = 587

assunto = 'Teste - Automatizar envio de emails'

# Assinatura HTML
assinatura_html = """
<div>
  <strong><font color="#0000ff">Polo de Ensino EAD | Universidade de Fortaleza - UNIFOR</font></strong><br>
  <img alt="📍" src="https://fonts.gstatic.com/s/e/notoemoji/16.0/1f4cd/32.png" width="16" height="16">
  <font color="#666666"> Bloco N | Campus UNIFOR | Fortaleza - CE</font><br>
  <img alt="📞" src="https://fonts.gstatic.com/s/e/notoemoji/16.0/1f4de/32.png" width="16" height="16">
  <font color="#666666"> (85) 3477-3479 | 0800-280-0550</font><br>
  <img alt="📧" src="https://fonts.gstatic.com/s/e/notoemoji/16.0/1f4e7/32.png" width="16" height="16">
  <font color="#666666"> <a href="mailto:curso.ead@unifor.br">curso.ead@unifor.br</a></font><br>
  <img alt="🌐" src="https://fonts.gstatic.com/s/e/notoemoji/16.0/1f310/32.png" width="16" height="16">
  <a href="https://www.unifor.br" target="_blank">www.unifor.br</a><br>
  <img alt="📅" src="https://fonts.gstatic.com/s/e/notoemoji/16.0/1f4c5/32.png" width="16" height="16">
  <font color="#666666">Atendimento: Segunda a sexta, 8h às 21h</font>
</div>
"""

# Corpo do e-mail em HTML
mensagem_html = f"""
<html>
  <body>
    <p>Olá,</p>
    <p>Esta é uma mensagem automática enviada via Python.</p>
    <p>Atenciosamente,<br>
    Yasmin Róseo - Auxiliar Administrativa</p>
    {assinatura_html}
  </body>
</html>
"""

# Envio dos e-mails
with smtplib.SMTP(smtp_server, smtp_port) as servidor:
    servidor.starttls()
    servidor.login(remetente, senha)

    for destinatario in emails:
        msg = MIMEMultipart("alternative")
        msg['From'] = remetente
        msg['To'] = destinatario
        msg['Subject'] = assunto

        # Corpo em HTML
        msg.attach(MIMEText(mensagem_html, 'html'))

        servidor.sendmail(remetente, destinatario, msg.as_string())
        print(f"E-mail enviado para {destinatario}")
