# Amazon Price Tracker 🇨🇦

A simple Python-based Amazon price tracker for Amazon.ca that monitors the price of a specific product and sends an email alert when the price drops below your target.

---

## 🚀 Features

- Uses **Selenium** with headless Chrome to access Amazon pages reliably
- Sends an email alert using **Gmail SMTP**
- Fully configurable product URL and target price
- Compatible with **Amazon Canada** and others
- Secure email credentials via `.env` file

---

## 🧱 Requirements

- Python 3.8 or higher
- Google Chrome (installed on your system)
- ChromeDriver (auto-managed via `webdriver-manager`)
- Gmail account (App Password required)

---

## 🔧 Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/Amazon-Price-tracker.git
   cd Amazon-Price-tracker

2. Install the required Python libraries:
   ```bash
   pip install requests beautifulsoup4
   pip install selenium webdriver-manager python-dotenv
   ```
3. **Create a .env file in the project root**
   ```bash
   EMAIL_ADDRESS=your_gmail@gmail.com
   EMAIL_PASSWORD=your_app_password_here
   ```   
4.  **How to Generate a Gmail App Password**
   - This is required if you use Gmail with 2-step verification enabled.
   - Go to: https://myaccount.google.com/apppasswords
   - Sign in to your Google account.
   - Under "Select app", choose Other (Custom name).
   - Enter a name like AmazonTracker and click Generate.
   - Copy the 16-character app password.
   - Paste it into your .env file as the EMAIL_PASSWORD.
## Usage

1. Open the script file and update the following:

   - Replace the `URL` variable with the Amazon product URL you want to track.
   - Replace `'youremail@gmail.com'` and `'Two_step_authentication_password'` with email address and the generated app password
   - Update the `convert < 100.0` condition with your desired price threshold.

2. Run the script:

   ```bash
   python amazon_price_tracker.py
   ```

3. If the price drops below the specified threshold, you will receive an email notification.

## Example Output

- Console Output:

  ```
  Product: Smeg DCGC01 Jug for Overflow Coffee Maker DCF02 DCG01, Glass
   Price: $51.0
   Email sent!
  ```

- Email Notification:

  ```
  Subject: Amazon Canada Price Drop Alert!
   The price of 'Smeg DCGC01 Jug for Overflow Coffee Maker DCF02 DCG01, Glass' has dropped to $51.0!
   Link: https://www.amazon.ca/Smeg-DCGC01-Replacement-Cup-Coffee/dp/B07YP1MZ9B  

  ```

## Notes

- Ensure that you enable "Less secure app access" or generate an app password for your email account if using Gmail.
- The script may need updates if Amazon changes its website structure.

## Disclaimer

This project is for educational purposes only. Scraping websites may violate their terms of service. Use this script responsibly.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
