import os
import smtplib
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from dotenv import load_dotenv

# Load email credentials
load_dotenv()
EMAIL = os.getenv("EMAIL_ADDRESS")
PASSWORD = os.getenv("EMAIL_PASSWORD")

# Amazon Canada product URL and your target price
URL = "https://www.amazon.ca/Smeg-DCGC01-Replacement-Cup-Coffee/dp/B07YP1MZ9B?psc=1"
TARGET_PRICE = 100.0  # Example: alert if below $100 CAD

# Set up Chrome options
options = Options()
# Comment out this line to see the browser open
# options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument(
    "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
)

driver = None

try:
    # Start browser
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.get(URL)

    # Wait for product title
    title_element = WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.ID, "productTitle"))
    )
    title = title_element.text.strip()

    # Try multiple known price locations
    price_xpaths = [
        '//*[@id="priceblock_ourprice"]',
        '//*[@id="priceblock_dealprice"]',
        '//*[@id="priceblock_saleprice"]',
        '//*[@class="a-price-whole"]',
    ]

    price = None
    for xpath in price_xpaths:
        try:
            element = driver.find_element(By.XPATH, xpath)
            price_text = element.text.strip().replace("$", "").replace(",", "").split('.')[0]
            price = float(price_text)
            break
        except:
            continue

    if price is None:
        raise Exception("Could not find the product price.")

    # Console output (dollar sign is ASCII-safe)
    print(f"Product: {title}")
    print(f"Price: ${price}")

    # If below target price, send email
    if price < TARGET_PRICE:
        subject = "Amazon Canada Price Drop Alert!"
        body = f"The price of '{title}' has dropped to ${price}!\n\nLink: {URL}"
        message = f"Subject: {subject}\n\n{body}"

        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(EMAIL, PASSWORD)
            server.sendmail(EMAIL, EMAIL, message)

        print("Email sent!")
    else:
        print("Price is still above your target.")

except Exception as e:
    print(f"Error: {e}")

finally:
    if driver:
        try:
            driver.quit()
        except:
            pass
