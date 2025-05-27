# email_service.py
import smtplib
from email.message import EmailMessage
import os


def send_report_email(to_email, attachments, logger=None):
    EMAIL_REMETENTE = "pedrohdosanjos@gmail.com"  # coloque seu email aqui
    SENHA = ""  # use senha de app para Gmail

    msg = EmailMessage()
    msg["Subject"] = "Relatórios gerados"
    msg["From"] = EMAIL_REMETENTE
    msg["To"] = to_email
    msg.set_content("Segue em anexo os relatórios gerados.")

    for arquivo in attachments:
        try:
            with open(arquivo, "rb") as f:
                data = f.read()
                nome = os.path.basename(arquivo)
                msg.add_attachment(data, maintype="image", subtype="png", filename=nome)
        except Exception as e:
            if logger:
                logger.error(f"Erro ao anexar arquivo {arquivo}: {e}")

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
            smtp.login(EMAIL_REMETENTE, SENHA)
            smtp.send_message(msg)
        if logger:
            logger.info(f"Email enviado para {to_email}")
        return True
    except Exception as e:
        if logger:
            logger.error(f"Erro ao enviar email: {e}")
        return False
