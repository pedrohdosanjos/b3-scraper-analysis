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
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. **Create a Google app password** to be used as the sender email's password.  
   This will allow the app to send emails without needing your main Google account password. To create an app password:

   - Go to your [Google Account Security Settings](https://myaccount.google.com/security).
   - Enable **2-Step Verification**.
   - Under "App passwords," generate a new password for "Other".
   - Copy the generated 16-character password.

4. Configure your email and app password in the `credentials.json` file:

   ```json
   {
     "email": "your_email@gmail.com",
     "password": "your_app_password"
   }
   ```

5. Run the application:

   ```bash
   python main.py
   ```

6. Enter your email address and click send.
