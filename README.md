# Personal Project - Data Analysis with Automation and Report Delivery

This is a personal project developed to practice data analysis through the automation of financial data collection, analysis, and report delivery.

---

## About the Project

This system performs:

- Automatic scraping of financial data from B3 (Brazilian Stock Exchange).  
- Data analysis with relevant tables and chart generation.  
- Sending reports via email, with charts embedded in the message body.  
- A simple graphical interface to enter the recipient's email and trigger the entire process.

---

## Technologies Used

- Python 3.8+  
- Pandas  
- Matplotlib  
- Selenium + WebDriver Manager  
- Tkinter  
- smtplib + email  

---

## Features

- Daily collection of stock prices and variations.  
- Automatic generation of tables and PNG charts.  
- Email delivery with images embedded and attached.  
- Intuitive interface to input email.  
- Logs for monitoring and debugging.

---

## How to Run

1. Clone this repository:  
   ```bash
   git clone https://github.com/pedrohdosanjos/b3-scraper-analysis.git
   cd b3-scraper-analysis

2. Install dependencies:
    ```bash
    pip install -r requirements.txt

3. Configure your email and app password in the credentials.json file:
    ```bash
    {
    "email": "your_email@gmail.com",
    "password": "your_app_password"
    }

4. Run the application:
    ```bash
    python main.py

5. Enter your email address and click send.
