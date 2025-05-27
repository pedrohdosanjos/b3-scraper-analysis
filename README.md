# Projeto Pessoal - Análise de Dados com Automação e Envio de Relatórios

Este é um projeto pessoal para automatizar a coleta, análise e envio de relatórios baseados em dados financeiros, desenvolvido para aprendizado prático na área de análise de dados.

---

## Sobre o Projeto

Este sistema realiza:

- Scraping automático de dados financeiros da B3.  
- Análise dos dados com geração de tabelas e gráficos relevantes.  
- Envio de relatórios por email, incluindo gráficos embutidos no corpo da mensagem.  
- Interface gráfica simples para interação, captura de email e disparo do processo completo.

---

## Tecnologias Utilizadas

- Python 3.8+  
- Pandas  
- Matplotlib  
- Selenium + WebDriver Manager  
- Tkinter  
- smtplib + email  

---

## Funcionalidades

- Coleta diária de cotações e variações de ações.  
- Geração automática de tabelas e gráficos em PNG.  
- Envio por email com imagens embutidas e anexadas.  
- Interface intuitiva para informar email.  
- Logs para monitoramento.

## Como Rodar

1. Clone este repositório:  
   ```bash
   git clone https://github.com/pedrohdosanjos/b3-scraper-analysis.git
   cd b3-scraper-analysis

2. Instale as dependências:
    ```bash
    pip install -r requirements.txt

3. Configure seu email e senha de aplicativo google no arquivo credentials.json
    ```bash
    {
    "email": "seu_email@gmail.com",
    "password": "sua_senha_de_app"
    }

4. Execute:
    ```bash
    python main.py

5. Informe seu email e clique em enviar.
