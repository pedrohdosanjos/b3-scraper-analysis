import tkinter as tk
from tkinter import messagebox
from scraper import run_scraper
from analysis import run_analysis
from email_service import send_report_email


def run_interface(logger):
    def on_click():
        email = entry_email.get().strip()
        if not email:
            messagebox.showerror("Erro", "Informe um email válido")
            return

        sucesso = iniciar_processos(logger, email)
        if sucesso:
            messagebox.showinfo("Sucesso", f"Processos concluídos para {email}")
        else:
            messagebox.showerror("Erro", "Falha no processamento.")

    root = tk.Tk()
    root.title("Executar Scraper e Análise")

    tk.Label(root, text="Digite seu email:").pack(padx=10, pady=10)
    entry_email = tk.Entry(root, width=40)
    entry_email.pack(padx=10)

    btn = tk.Button(root, text="Iniciar", command=on_click)
    btn.pack(pady=20)

    root.mainloop()


def iniciar_processos(logger, email):
    try:
        run_scraper(logger)
        run_analysis(logger)
    except Exception as e:
        logger.error(f"Erro ao rodar scraper ou análise: {e}")
        return False

    arquivos = [
        "data/tabela_altas.png",
        "data/tabela_baixas.png",
        "data/grafico_ocorrencias.png",
    ]

    sucesso_email = send_report_email(email, arquivos, logger)
    if not sucesso_email:
        logger.error("Falha ao enviar email")
    return sucesso_email
