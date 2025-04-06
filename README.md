# Amazon-Price-tracker

This is a basic Amazon price tracker that monitors the price of a specific product on Amazon and sends an email notification when the price drops below a specified threshold.

## Features

- Scrapes product details (title and price) from Amazon using `BeautifulSoup`.
- Sends an email notification when the price falls below the desired amount.
- Easy to configure and customize.

## Prerequisites

- Python 3.x installed on your system.
- Required Python libraries: `requests`, `bs4`, and `smtplib`.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/Amazon-Price-tracker.git
   cd Amazon-Price-tracker
   ```

2. Install the required Python libraries:
   ```bash
   pip install requests beautifulsoup4
   ```

## Usage

1. Open the script file and update the following:

   - Replace the `URL` variable with the Amazon product URL you want to track.
   - Replace `'youremail@gmail.com'` and `'Two_step_authentication_password'` with your email credentials.
   - Update the `convert < 220000.00` condition with your desired price threshold.

2. Run the script:

   ```bash
   python amazon_price_tracker.py
   ```

3. If the price drops below the specified threshold, you will receive an email notification.

## Example Output

- Console Output:

  ```
  219999.00
  Apple MacBook Pro (15-inch, 2018)
  ```

- Email Notification:

  ```
  Subject: Price fell down !!

  Here's the link https://www.amazon.in/Apple-MR972HN-15-4-inch-i7-8850H-Integrated/dp/B07G49GQ56/ref=sr_1_4?keywords=macbook+pro&qid=1576257615&sr=8-4
  ```

## Notes

- Ensure that you enable "Less secure app access" or generate an app password for your email account if using Gmail.
- The script may need updates if Amazon changes its website structure.

## Disclaimer

This project is for educational purposes only. Scraping websites may violate their terms of service. Use this script responsibly.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
