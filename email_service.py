# email_service.py
import json
import smtplib
from email.message import EmailMessage
from email.utils import make_msgid
import os


def send_report_email(to_email, image_paths, logger=None):
    with open("credentials.json", "r") as f:
        credentials = json.load(f)
        EMAIL_REMETENTE = credentials.get("email")
        SENHA = credentials.get("password")

    msg = EmailMessage()
    msg["Subject"] = "Relatórios gerados"
    msg["From"] = EMAIL_REMETENTE
    msg["To"] = to_email

    # Criar IDs únicos para as imagens
    cids = [make_msgid(domain="example.com")[1:-1] for _ in image_paths]

    # Montar corpo HTML com as imagens embutidas via cid
    html_content = "<h2>Relatórios gerados</h2><br>"
    for cid in cids:
        html_content += f'<img src="cid:{cid}" style="max-width:900px;"><br><br>'

    msg.add_alternative(html_content, subtype="html")

    # Anexar imagens com Content-ID
    for path, cid in zip(image_paths, cids):
        try:
            with open(path, "rb") as img:
                data = img.read()
                msg.get_payload()[0].add_related(
                    data, maintype="image", subtype="png", cid=cid
                )
        except Exception as e:
            if logger:
                logger.error(f"Erro ao anexar imagem {path}: {e}")

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
